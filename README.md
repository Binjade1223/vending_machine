# vending_machine
intern project in iii.

--- Environment setup ---

* Use Raspberry pi3

(1) apt-get

sudo apt-get update

sudo apt-get upgrade

(2) update kernel

sudo rpi-update

(3) turn on SPI

sudo raspi-config
(>>>turn on the SPI service)

(4) add some text in /boot/config.txt

sudo nano /boot/config.txt
(dtoverlay=spi0-hw-cs)

(5) reboot

sudo reboot now

(6) check 24-pin

gpio readall
(check: "24 | 1 | ALT0 | CE0 | 10 | 8 | ". if not, should setup carefully again.)

(7) install some tools & packages

cd ~

sudo apt-get install -y python-dev

git clone https://github.com/lthiery/SPI-Py.git

cd SPI-Py

sudo python setup.py install

cd ..

git clone https://github.com/Binjade1223/vending_machine


--- Application ---

cd vending_machine

python main.py
