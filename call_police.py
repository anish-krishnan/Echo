import string
import RPi.GPIO as GPIO
import time


from num2words import num2words
from subprocess import call
from email_server import *
import smtplib

cmd_beg= 'espeak '
cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
cmd_out= '--stdout > /home/pi/Desktop/Text.wav ' # To store the voice file
alarm='"Police alerted"'

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def notify(pill, address): 
    fromaddr = "pharmabot4@gmail.com"
    toaddr = address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "ECHO NOTIFICATION"
    body = "YOUR ELDERLY" + pill + "IS IN DISTRESS. PLEASE COME TO THE UNIVERSITY OF PENNSYLVANIA SEAS BUILDING"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(fromaddr, "pharmabot44")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)



while True:
    input_state = GPIO.input(18)
    if input_state == True:
        call([cmd_beg+alarm+cmd_end], shell=True)
        notify("SENIOR CITIZEN: MICHAEL LI", "michaelli1234@gmail.com")
        time.sleep(0.5)
    
