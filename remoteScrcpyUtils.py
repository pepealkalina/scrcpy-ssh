'''
Filename: remoteScrcpySSH.py
Created Date: Friday, May 9th 2025, 10:27:13 am
Author: Pepe Alkalina
'''

from scrcpy import Client, EVENT_FRAME
import cv2
import sys
from threading import Thread
from paramiko import SSHClient, WarningPolicy, Transport
from paramiko_demos.forward import forward_tunnel
from paramiko_demos.rforward import reverse_forward_tunnel


windowName=""


## Establece la connexion ssh y aplica la tunelización
def connectSSH(host, user, password):
    # define ssh connection basic parametres
    sshHost = host
    sshPort = 22
    sshUser = user
    sshPasswd = password

    # configure a ssh client
    sshConn = SSHClient()
    sshConn.set_missing_host_key_policy(WarningPolicy())

    # stablish a ssh connection
    sshTransport = Transport((sshHost, sshPort))

    # Command for paramiko-1.7.7.1
    sshTransport.connect(hostkey  = None,
                    username = sshUser,
                    password = sshPasswd,
                    pkey     = None)
    try:
        tunnel = Thread(target=forward_tunnel, args=(5037, '127.0.0.1', 5037, sshTransport))
        # forward_tunnel(5037, '127.0.0.1', 5037, sshTransport)
        tunnel.start()
        reverse_tunnel = Thread(target=reverse_forward_tunnel, args=(27183, '127.0.0.1', 27183, sshTransport))
        # reverse_forward_tunnel(27183, '127.0.0.1', 27183, sshTransport)
        reverse_tunnel.start()
    except KeyboardInterrupt:
        sys.exit(0)

def onFrameScreen(frame):
    if frame is not None:
        cv2.imshow(windowName,frame)
        cv2.waitKey(0)
        


def scrcpyConnect(serial):
    windowName=serial
    client = Client(device=serial)
    client.add_listener(EVENT_FRAME, onFrameScreen)
    client.start()
    

def connectScrcpySSH():
    connectSSH('10.11.23.166', 'morse', 'lab333')
    scrcpyConnect(serial="f17f8091")

if __name__ == '__main__':
    connectScrcpySSH()

