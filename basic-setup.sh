#!/bin/bash
# Ubuntu Developer Script For Initial-Ubuntu-Setup
# Created by Sourabh-Singh.
#   chrome
#   sublime
#   git
#   terminator
#   zsh
#   oh-my-zsh
#	variety
#	pip

#chrome
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt-get update
sudo apt-get install google-chrome-stable -y

#sublime
sudo add-apt-repository ppa:webupd8team/sublime-text-2 -y
sudo apt-get update
sudo apt-get install sublime-text -y

#git
sudo apt-get update
sudo apt-get install git -y

#terminator
sudo apt-get update
sudo add-apt-repository ppa:gnome-terminator -y
sudo apt-get update
sudo apt-get install terminator -y

#zsh
sudo apt-get install zsh -y

#oh-my-zsh
wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh

#variety
sudo add-apt-repository ppa:peterlevi/ppa -y
sudo apt-get update
sudo apt-get install variety -y

#pip
sudo apt-get install python-pip -y
