# ALStatus
Azur Lane Server Status Monitor


This python script checks the server status of Azur Lane, if any changes is detected, a message with details will be sent via discord webhook.

**Currently, Only JP Server is supported due to the fact I'm too lazy to download other regions and check for the url responsible for statuses**


# Dependencies

**1. Discord Webhook**
`pip3 install discord-webhook`

# How to Use
1. Use crontab if you're hosting it on an linux server
2. Use task scheduler if you're hosting it on windows
3. Schedule the script to run every **X** intervals
4. Profit?
