#!/bin/bash

# This ended up being the easiest way to manage deployment when working from Windows
# and deploying to a remote target with an architecture that isn't supported by VS
# Code's remote SSH extension and further complicated by using a password protected
# ssh key for authentication

rsync -avz ./ pi@terrarium.home.arpa:/home/pi/terrarium