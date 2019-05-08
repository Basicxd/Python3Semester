import time
from socket import *
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(3, GPIO.OUT)

BROADCAST_TO_PORT = 7000
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.bind(('', 0))


def sensorLoop():
    i = GPIO.input(7)
    if i == 0:
        return "No intruders",i
    elif i == 1:
        return "intruders here",i
    else:
        return "Something went wrong"



now = datetime.now()

while True:
    data = "Actions: " + str(sensorLoop()) + '\n' + "Time: " + str(now.strftime("%m/%d/%Y, %H:%M:%S"))  # + '\n' add if needed
    s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    print(data)
    time.sleep(1)
