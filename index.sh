#!/bin/sh
fab setup
echo "-----------------------------------Setup Complete----------------------------------"
source ./msisdn-cli/.venv/bin/activate
echo "---------------------------Virtual Environment Activated---------------------------"
python ./control-script/control-script.py
echo "------------------------------------Completed Test---------------------------------"
deactivate
echo "------------------------------------Begin Teardown---------------------------------"
fab teardown