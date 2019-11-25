#!/bin/bash

echo -e "Please enter your IoT Edge Device Connection String: "
read deviceConnString
echo "Device:  $deviceConnString"

echo "Download and install the moby-engine"
curl -L https://aka.ms/moby-engine-armhf-latest -o moby_engine.deb && sudo dpkg -i ./moby_engine.deb

echo "Download and install the moby-cli"
curl -L https://aka.ms/moby-cli-armhf-latest -o moby_cli.deb && sudo dpkg -i ./moby_cli.deb

echo "Run apt-get fix"
sudo apt-get install -f

echo "Download and install the standard libiothsm implementation"
curl -L https://aka.ms/libiothsm-std-linux-armhf-latest -o libiothsm-std.deb && sudo dpkg -i ./libiothsm-std.deb

echo "Download and install the IoT Edge Security Daemon"
curl -L https://aka.ms/iotedged-linux-armhf-latest -o iotedge.deb && sudo dpkg -i ./iotedge.deb

echo "Run apt-get fix"
sudo apt-get install -f

echo "Update config.yaml"
sudo sed -i "s/\"<ADD DEVICE CONNECTION STRING HERE>\"/\""$deviceConnString"\"/" /etc/iotedge/config.yaml

echo "Restart IoT Edge Runtime"
sudo systemctl restart iotedge