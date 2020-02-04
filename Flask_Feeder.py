#!/usr/bin/python3

import PiMotor as PiMotor
import time
import RPi.GPIO as GPIO

#Import standard
import logging, os, time

#Import Flask and Flask Ask for Amazon
from flask import Flask
from flask_ask import Ask, request, session, question, statement

#Set App Name and Log App Details
app = Flask(__name__)
ask = Ask(app,"/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.launch
def launch():
    speech_text='Welcome to the automation Project by JND to feed you animals using Alexa'
    return question(speech_text).repromt(speech_text).simple_card(speech_text)

@ask.intent('GpioIntent', mapping = {'status':'status'})
def GPIO_Intent():
    #Assign Motor
    m1 = PiMotor.Motor("MOTOR1",1)

    #Turn the Motor
    m1.forward(100)

    #Wait 5 Seconds
    time.sleep(3)

    #Turn the Motor
    m1.reverse(100)

    #Wait 1 Seconds
    time.sleep(1)

    #Stop
    m1.stop()

    return statement('Dogs Fed')

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
