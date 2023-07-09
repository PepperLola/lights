#!/bin/bash
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt-get update && sudo apt-get -y upgrade
    sudo apt-get -y install quilt qemu-user-static debootstrap zip libarchive-tools qemu-tools git curl grep
    git clone https://github.com/PepperLola/lights-pi-gen.git
    cd lights-pi-gen
    chmod +x build.sh
    cd ..
else
    echo "Can only build images on a Raspberry Pi running Ubuntu!"
fi
