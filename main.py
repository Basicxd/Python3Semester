import time
from socket import *
from datetime import datetime

BROADCAST_TO_PORT = 7000
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.bind(('', 0))


def test(x):
    i = x
    if i == 0:
        return "No intruders"
    elif i == 1:
        return "intruders here"
    else:
        return "something went wrong"



now = datetime.now()

while True:
    data = "Actions: " + str(test(0)) + '\n' + "Time: " + str(now.strftime("%m/%d/%Y, %H:%M:%S"))  # + '\n' add if needed
    s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    print(data)
    time.sleep(1)
