# Python_Alexa_RaspberryPi_Automation
This repo tutorial is how to use Alexa to trigger a Python Script on a remote Raspberry Pi to turn on a motor. The motor is mounted on a 40lbs dog food dispenser. A user triggers Alexa to run the script by saying "Alexa, ask Raspberry Pi to feed the dogs". Amazon will send a signal to the ngrok endpoint which tunnels to our Flask app. Flask will interpet the intent response, triggering the motor to turn forward for a defined duration of time, then reversing the motor direction to stop the flow of food. This Repo is an end-to-end small scale example of combining Python and hardware for real world physical automation.  


In an ideal scenario the 'motor' script can be set to be executed by a cron job to ensure feeding happens automatically at a defined time, daily. In an ideal scenario, Alexa, Ngrok, and Flask are uneeded. This example is to 'wow your friends' and show the possiblities of creativity and a 'can do' attitude.  

## Getting Started
Make sure you have the products below and a host computer for initial install and flash of Raspbian on the Raspberry Pi. 



### Products Used


### High Level Steps:
1. Boot Raspberry Pi with Raspbian 
2. Install Python3 and packages
3. Add Python Scripts  (Flask_Ask Script.py and Motor.py)
4. Connect Motor, Battery Pack, and Hat to Pi (test the motor working by executing Motor.py)
5. Download and Install Ngrok and Ngrok Account
6. Create Amazon Dev Account
7. Add Json and Ngrok EndPoint
8. Test commands on Alexa or Amazon Developer Console 

## 1. Raspberry Pi setup

*[Flash Raspbian to your RaspberryPi](https://www.raspberrypi.org/documentation/installation/installing-images) 

I operate on a Mac and followed the steps below outlined by the raspberry pi org. I used this method beacuse I wanted to install and run the Pi headless. 

Download [balenaEtcher](https://www.balena.io/etcher) and install it.
Connect an SD card reader with the SD card inside.
Open balenaEtcher and select from your hard drive the Raspberry Pi .img or .zip file you wish to write to the SD card.
Select the SD card you wish to write your image to.
Review your selections and click 'Flash!' to begin writing data to the SD card.

(I would recommend using [NOOBS](https://www.raspberrypi.org/documentation/installation/noobs.md) if you have an extra monitor/HDMI cables, keyboard, and mouse.)

Since running the Pi headless I needed to create two files. One to ssh into the Pi and the other to define the network WIFI connection.

Unix Commands
```bash
jdavis@Mac:~$ touch /Volumes/boot/ssh
jdavis@Mac:~$touch /Volumes/boot/wpa_supplicant.conf
jdavis@Mac:~$sudo nano /Volumes/boot/wpa_supplicant.conf
```
Add Network Credentials to wpa_supplicant.conf

```bash
country=US
network={
    ssid="NETWORK-NAME"
    psk="NETWORK-PASSWORD"
}
```

Eject micro SD card, place in Pi, boot Pi.
Confirm you can ssh into Pi with the following command.

```bash
ssh pi@raspberrypi.local
```
I highly recommend using sudo raspi-config in order to change your password and host name after you ssh the first time. 

## Install Python3, Packages, and Scripts

To install Python3 and the required packages run the commands below.

```bash
ssh pi@raspberrypi.local
pi@raspberrypi.local:~$ sudo apt-get install python3
pi@raspberrypi.local:~$ python3 -m pip install flask_ask, cryptography==2.1.4
```
Create the Motor Directory and the Python Files

```bash
pi@raspberrypi.local:~$ cd ~
pi@raspberrypi.local:~$ mkdir Motor
pi@raspberrypi.local:~$ cd Motor
pi@raspberrypi.local:~$ touch Flask_App_Feeder.py
pi@raspberrypi.local:~$ touch Motor.py
```
Open the 'Flask_App_Feeder.py' by using 
```bash
pi@raspberrypi.local:~$ sudo nano Flask_App_Feeder.py
```
and insert the following Python Code

```python
import os
```

Open the 'Motor.py' by using 
```bash
pi@raspberrypi.local:~$ sudo nano Motor.py
```
and insert the following Python Code

```python
import os
```
Save and close both files.

## Ngrok

## 




## Running the Flask_App File


## Deployment


## Built With

* [Jupyter](https://jupyterhub.am.lilly.com) - Web Interface to HPC Linux environments
* [Apache](https://maven.apache.org/) - Dependency Management


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

I use [GitHub](https://github.com/James-Davis-JnD/Python_Alexa_RaspberryPI_Automation) for versioning. For the versions available, see the [tags on this repository](https://github.com/James-Davis-JnD/Python_Alexa_RaspberryPI_Automation/tags). 

## Authors

* **James N. Davis** - *Initial work* - [James Nathan Davis](https://www.linkedin.com/in/james-davis-a13b4378)

## License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
 





