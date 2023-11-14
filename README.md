## Linux-sensors-telegram-notification

First clone the repository
```
git clone https://github.com/youonmyown/linux-sensors-telegram-notification.git
```
### Execute Python script via crontab
run the command in console:
```
crontab -e
```
Add this to the end of the file:
```
0 * * * * /usr/bin/python /path_to_file/main.py
```
The script will run once per hour at 0 minutes

Use this service to change your scheduler:
https://crontab.guru/
