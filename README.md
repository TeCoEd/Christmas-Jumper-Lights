# Christmas Jumper Lights
# Tweet @PiTests ON to trigger the "XMAS Jumper" to light up in full festive glory.

This hack makes use of:
- an old Christmas Jumper, 
- the Raspberry Zero, 
- some cheap LEDs 
- a bit of Python 

The combination brings you an Interactive Social Media Crimbo Jumper.  Tweet "@PiTests ON" and the code kicks in.  It triggers the lights on the jumper to turn on and the light show begins.  So now all Twitter users can bring a little bit of Christmas cheer and engage the lights on the Jumper.  To thank you for your efforts the "Light Bot" will send you a confirmation message via your tweeter feed. You will receive a notification that you turned on the Christmas Light Jumper including the time of your interaction.

The Pi Zero uses a WiFi dongle and is tethered to a mobile phone to ensure that the Jumper is mobile and can be interactive when out and about.  WiFi management was disabled to ensure that the WiFi connection does not drop out at any point.

This was a set up using:  **sudo nano /etc/network/interfaces**
Then add the line:        **wireless-power off**

Save the file and reboot the Pi

Finally, the program is running on a Pi Zero and needs to be headless, also you will probably not be carrying a display around with you.  Plugging in the power to the Pi Zero starts up the program and runs it. 

To enable this type: **sudo nano /etc/rc.local**
Add the location of the program for example, **python /home/pi/LED_Jumper.py &**

Save the program and restart the Pi Zero.

**Happy Christmas**

Project website: http://www.tecoed.co.uk/crimbo-lights-hack.html

(This has also been adapted to create a LED Hat)

