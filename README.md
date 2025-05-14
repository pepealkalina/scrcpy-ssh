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

## Setting up an Usage

### Setting up

> [!IMPORTANT]
> You need python 3.10 and pip installed for setting up the project, if there is any problem with the packages installation install it manually

To set up the project follow the following steps:

1. Create with `venv` a virtual enviroment and activate it
    ```
    $> python3.10 -m venv <path-of-venv>
    $> source <path-of-venv>/bin/activate
    ```

2. Install the packages in `requirements.txt` with pip
    ```
    $> pip install -r requirements.txt
    ```

Then you can use the script if there is some troubles, these are the packages to install they manually

* `paramiko`: For ssh management
* `scrcpy-client`: For scrcpy client mangement
* `PySide6`: For show window management
* `cx-Freeze`: For creates the binary

> [!NOTE]
> Pip is supposed to install all dependencies, so if there is a problem, check the package dependencies.


### Variables to change

In `createExec.py` you need to change some global variable to configure the ssh conection, user creation and binary generation.

* `serverIP`: Is the scrcpy and ssh server IP
* `sshSudoUser` and `sshSudoPasswd`: Are the sudo credential of the linux server for create the user
* `appIconFile`: If you want to generate a `.app` MacOS file and give it an icon set the path of the icon here
* `dist`: set buid distribution for the binary

### Usage

The use of the script is simple once everything is set up you just need to run the following:
```
$> python createExec.py
```

> [!NOTE]  
> In linux you may have to use python3 instead of python

## External Code

For this project I have used a couple of demos from <a href="https://github.com/paramiko/paramiko/tree/main/demos">paramiko</a>, to create the ssh tunnels, they are included in the `paramiko_demos` folder.


