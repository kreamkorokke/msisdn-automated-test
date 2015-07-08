#!/bin/sh
fab setup || exit 1
echo "-----------------------------------Setup Complete----------------------------------"
source ./msisdn-cli/.venv/bin/activate
echo "---------------------------Virtual Environment Activated---------------------------"
python ./msisdn-automated-test/control-script.py
echo "------------------------------------Completed Test---------------------------------"
deactivate
echo "------------------------------------Begin Teardown---------------------------------"
fab teardown || exit 1