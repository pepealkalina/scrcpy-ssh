'''
Filename: remoteScrcpySSH.py
Created Date: Friday, May 9th 2025, 10:27:13 am
Author: Pepe Alkalina
'''

from scrcpy import Client, EVENT_FRAME
from createWindow import *
import cv2
import sys
from threading import Thread, Event
from paramiko import SSHClient, WarningPolicy, Transport
from paramiko_demos.forward import forward_tunnel
from paramiko_demos.rforward import reverse_forward_tunnel
from PySide6.QtGui import QImage, QKeyEvent, QMouseEvent, QPixmap, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

if not QApplication.instance():
    app = QApplication([])
else:
    app = QApplication.instance()


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

    stopEvent = Event()
    try:
        tunnel = Thread(target=forward_tunnel, args=(5037, '127.0.0.1', 5037, sshTransport))
        # forward_tunnel(5037, '127.0.0.1', 5037, sshTransport)
        tunnel.start()
        print('a')
        reverseTunnel = Thread(target=reverse_forward_tunnel, args=(27183, '127.0.0.1', 27183, sshTransport))
        # reverse_forward_tunnel(27183, '127.0.0.1', 27183, sshTransport)
        reverseTunnel.start()
        print('b')
    except KeyboardInterrupt:
        sys.exit(0)

class ConnectScrcpy(QMainWindow):
    def __init__(self, serial: str):
        super().__init__()
        self.setWindowTitle("Serial: " + serial)
        self.client = Client(device=serial)
        self.windowName=serial
        self.client.add_listener(EVENT_FRAME, self.onFrame)
        self.label = QLabel()
        self.label.setFixedSize(360, 800)
        self.label.setScaledContents(True)
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def onFrame(self, frame):
        app.processEvents()
        if frame is not None:
            image = QImage(
                frame,
                frame.shape[1],
                frame.shape[0],
                QImage.Format_BGR888,
            )
            pix = QPixmap(image)
            self.label.setPixmap(pix)
    
    def closeEvent(self, _):
        self.client.stop()
        

def connectScrcpySSH():
    connectSSH('10.11.23.166', 'morse', 'lab333')
    print('c')
    mainWin = ConnectScrcpy("f17f8091")
    mainWin.show()
    mainWin.client.start()
    



if __name__ == '__main__':
    connectScrcpySSH()

