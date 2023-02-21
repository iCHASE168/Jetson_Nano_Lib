# Install yolov4

1. Update

```shell
sudo apt-get -y update
```

3. Export Cuda path

```shell
export PATH=/usr/local/cuda-10.2/bin${PATH:+:${PATH}}
```

```shell
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

3. Download Darknet and Yolo

```shell
git clone https://github.com/AlexeyAB/darknet
```

# Change the parameters and compile

1. Edit makefile:

```shell
cd darknet
sudo apt -y install nano
sudo nano Makefile
GPU =1
CUDNN=1
OPENCV=1
LIBSO = 1  !!!!!
```

2. Compile the darknet:

```shell
make
```

# Install the package in need

1. Install pip3

```shell
sudo apt-get install python3-pip python3-dev
```

2. Install python module

```shell
pip3 install spidev
pip3 install pyserial
pip3 install openpyxl
pip3 install smbus 
pip3 install requests
pip3 install schedule
pip3 install psutil
```

3.Install jtop

```shell
sudo -H pip3 install jetson-stats
```

# Enable the function in need

1. Config the GPIO function

```shell
# enable spi1 and spi2 PIN function
sudo /opt/nvidia/jetson-io/jetson-io.py
```

2. Enable the VNC

```shell
cd /usr/lib/systemd/user/graphical-session.target.wants
sudo ln -s ../vino-server.service ./.
gsettings set org.gnome.Vino prompt-enabled false
gsettings set org.gnome.Vino require-encryption false
# Replace thepassword with your desired password
gsettings set org.gnome.Vino authentication-methods "['vnc']"
gsettings set org.gnome.Vino vnc-password $(echo -n 'thepassword'|base64) # replace the 'thepassword' with the password
```

# Install Teamviewer

```shell
https://www.teamviewer.com/tw/download/raspberry-pi/
cd ./Downloads
sudo dpkg -i "teamviewer-host_15.28.6_arm64.deb"
sudo apt -y install -f
```

# useful software (Not necessary)

1. vscode

```shell
 git clone https://github.com/JetsonHacksNano/installVSCode.git
 cd installVSCode
./installVSCode.sh
```

