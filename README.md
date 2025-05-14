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



