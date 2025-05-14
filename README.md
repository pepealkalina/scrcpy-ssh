# REMOTE-SCRCPY-SSH

Connects to a scrpcy server via ssh tunneling by port forwarding.

## Description
This python script automates the following process:

* In bash or powershell
    ```bash
    $> ssh -CN -L5037:127.0.0.1:5037 -R27183:127.0.0.1:2718 <user>@<server-IP>
    ```
* In other terminal
    ```bash
    $> adb devices
    List of devices attached
    <serial>	device

    $> scrcpy --port 27183 --serial <serial>
    ```

> [!NOTE]
> The serial is given by adb devices, it the usb serial, is not equal to mobile serial

<br>

This scripts shows a simple tkinter UI which asks you to enter the new user name, password, account expiry date and device serial.

The user then remotely creates via ssh a temporary user whose account expires on the date provided.

And finally it generates a binary which allows us to do the above automation without the need to enter a username and password.

## Variables to change

In `createExec.py` you need to change some global variable to configure the ssh conection, user creation and binary generation.

* `serverIP`: Is the scrcpy and ssh server IP
* `sshSudoUser` and `sshSudoPasswd`: Are the sudo credential of the linux server for create the user
* `appIconFile`: If you want to generate a `.app` MacOS file and give it an icon set the path of the icon here
* `dist`: set buid distribution for the binary

## External Code

For this project I have used a couple of demos from <a href="https://github.com/paramiko/paramiko/tree/main/demos">paramiko</a>, to create the ssh tunnels, they are included in the `paramiko_demos` folder.


