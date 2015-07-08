#!/bin/sh
fab setup || exit
echo "-----------------------------------Setup Complete----------------------------------"
source ./msisdn-cli/.venv/bin/activate || exit
echo "---------------------------Virtual Environment Activated---------------------------"
python ./control-script/control-script.py || exit
echo "------------------------------------Completed Test---------------------------------"
deactivate || exit
echo "------------------------------------Begin Teardown---------------------------------"
fab teardown || exit