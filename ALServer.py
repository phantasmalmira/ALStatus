import requests as r
import json
import io
from discord_webhook import DiscordWebhook, DiscordEmbed

state_url = "http://blhxjploginapi.azurlane.jp/?cmd=load_server?"
state = {
    0: "**Online**",
    1: "**Offline**"
}

discord_api = {
    "web_hook": "WEBHOOK URL HERE",
    "mention": "<@&MENTION ROLE ID HERE>"
}


def update_json(string: str):
    with io.open("ALServer.json", mode="w", encoding="utf-8") as f:
        f.write(string)
    f.close()


def get_json_data(string: str):
    return json.loads(string)


def fetch_new_json():
    try:
        blhx_raw = r.get(state_url).text
    except ConnectionError:
        print("Connection Failed, aborting script")
        exit(1)
    return blhx_raw


def fetch_old_json():
    error_old = False
    try:
        f = io.open("ALServer.json", mode="r", encoding="utf-8")
        blhx_raw_old = f.read()
        f.close()
        if blhx_raw_old == None:
            error_old = True
        else:
            return blhx_raw_old
    except FileNotFoundError:
        error_old = True
    if error_old:
        update_json(fetch_new_json())
        exit()


def state_change_check():
    message_to_print = "**SERVER STATUS**\n"
    new_states = get_json_data(fetch_new_json())
    old_states = get_json_data(fetch_old_json())
    changed = False
    for index in range(len(new_states)):
        if new_states[index]["state"] != old_states[index]["state"]:
            message_to_print = message_to_print + new_states[index]["name"] + " had gone from " + state[old_states[index]["state"]] + " to " + state[new_states[index]["state"]] + "\n"
            changed = True
    if changed:
        update_json(fetch_new_json())
        send_alert_discord(message_to_print)


def send_alert_discord(message: str):
    web_hook = DiscordWebhook(url=discord_api["web_hook"], content=discord_api["mention"])
    embed = DiscordEmbed(title='Azu chan\'s news!', description=message, color=1699843)
    # embed.set_image(url='https://cdn.discordapp.com/emojis/554398006045311014.png')
    embed.set_footer(text='Time now')
    embed.set_timestamp()
    web_hook.add_embed(embed)
    web_hook.execute()


state_change_check()
