showMEtheIP
===========

Gives you the ip address of your raspberry pi at startup

To run this file at startup, use either the crontab or /etc/rc.local

Using crontab:
>sudo crontab -e

>scroll to the bottom and add @reboot sudo python /home/pi/iptest.py &

Using /etc/rc.local
>sudo nano /etc/rc.local

>enter sudo python /home/pi/iptest.py before the line that reads 'exit 0'

Both methods have worked for me

*Note: this script is designed specifically to work with gmail
