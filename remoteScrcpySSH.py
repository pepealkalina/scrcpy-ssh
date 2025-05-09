'''
Filename: remoteScrcpySSH.py
Created Date: Friday, May 9th 2025, 10:27:13 am
Author: Pepe Alkalina
'''

from scrcpy import Client, EVENT_FRAME
from adbutils import adb
from cv2 import imshow, waitKey

import paramiko

def createSSHTunneling():
    sshConn = paramiko.SSHClient()
    sshConn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshConn.connect('10.11.23.166', username='morse', password='lab333')

    adbForward = sshConn.get_transport()

    adbLocalPort = 5037
    adbRemoteHo = 5037



def onFrameScreen(frame):
    if frame is not None:
        imshow("morse scrcpy",frame)
    waitKey(10)

def scrcpyConnect(serial):
    print(serial)
    client = Client(device=serial)
    client.add_listener(EVENT_FRAME, onFrameScreen)
    client.start()

def main():
    scrcpyConnect(serial=adb.device_list()[0])

if __name__ == '__main__':
    main()



