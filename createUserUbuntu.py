'''
Filename: createUserUbuntu.py
Created Date: Tuesday, May 13th 2025, 8:41:43 am
Author: Pepe Alkalina
'''

import paramiko

def createUserSSH(user, password, expirationDate, sshUser, sshPasswd, sshIP):
    
    sshConn = paramiko.SSHClient()
    sshConn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    sshConn.connect(sshIP, port='22', username=sshUser, password=sshPasswd)

    userAdd = "sudo -S -p '' useradd " + user
    stdin, stdout, stderr = sshConn.exec_command(userAdd)
    stdin.write(sshPasswd + "\n")

    changePasswd = f"sudo -S -p '' usermod --password $(echo {password} | openssl passwd -1 -stdin) {user}"
    stdin, stdout, stderr = sshConn.exec_command(changePasswd)
    stdin.write(sshPasswd + "\n")

    changeExpireDate = "sudo -S -p '' chage -E " + expirationDate + " " + user
    stdin, stdout, stderr = sshConn.exec_command(changeExpireDate)
    stdin.write(sshPasswd + "\n")

    sshConn.close()