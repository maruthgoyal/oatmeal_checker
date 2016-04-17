#!/bin/bash

echo "Please enter your password to continue. It is required to install the following setup tools: PIP, VIRTUALENV"

# Installing pip and virtualenv system-wide
sudo -H easy_install pip
sudo pip install virtualenv

# Installing Homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Installing terminal-notifier (For Desktop Notifications)
brew install terminal-notifier

#Setting up the virtual environment to avoid installing libraries system wide unnecesarily
virtualenv venv
source venv/bin/activate
pip install beautifulsoup4

# Deactivating virtualenv
deactivate
