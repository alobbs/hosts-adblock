#!/usr/bin/env python3

import os

# Move to the script directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Update list
os.system("./hosts-adblock.py")

# Push to Github is needed
with os.popen("git add hosts-adblock-alobbs") as f:
    has_update = len(f.read()) > 1

if has_update:
    os.system("git add hosts-adblock-alobbs")
    os.system('git commit -m "Updates list of domains"')
    os.system("git push")
