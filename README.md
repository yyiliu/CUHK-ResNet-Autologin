# CUHK-ResNet-Autologin
CUHK Hostel Network Auto Authenticator

### Usage

Deploy in a sleepless server, e.g., Raspberry Pi, or your PC.

Modify `autowifi.py` accordingly.

1. Direct run

    Start:

    ```bash
    nohup python autowifi.py &
    ```

    Stop:

    Find the PID in the log file.

    ```bash
    kill [PID]
    ```

2. Controlled by systemd

    Modify `autowifi.service` accordingly.

    Move `autowifi.service` to `/etc/systemd/system`.

    Start:

    ```bash
    sudo systemctl start autowifi.service
    ```

    Stop:

    ```bash
    sudo systemctl stop autowifi.service
    ```

    

​	

​	