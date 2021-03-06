#!/bin/sh
fab setup || exit 1
echo "-----------------------------------Setup Complete----------------------------------"
echo "---------------------------Virtual Environment Activated---------------------------"
python ./msisdn-automated-test/control-script.py -a ${ACCOUNT_AUTH} -n ${NUMBERS}
echo "------------------------------------Completed Test---------------------------------"
echo "------------------------------------Begin Teardown---------------------------------"
fab teardown || exit 1
echo "-----------------------------------Finished Teardown-------------------------------"
echo "---------------------------Virtual Environment Deactivated-------------------------"
deactivate
rm -fr venv