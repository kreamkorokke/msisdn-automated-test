#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect
import sys
import time
import re
from twilio.rest import TwilioRestClient

host = "https://msisdn.services.mozilla.com"
host_number = "+12182967993"
mccs = ["310"]
numbers = ["+16502650808"]
account_sid = "ACea6b158b0109812803f02e90e026fa0c"
auth_token = "b6c0cf4ac5b0c28b681a490b16f352a2"
client = TwilioRestClient(account_sid, auth_token)

def clean_up_message_logs():
	# clean up the previous message logs
	messages = client.messages.list()
	for i in range(0, len(messages)):
		client.messages.delete(messages[i].sid)

def run_msisdn_cli(cli_command, gateway_number, test_number):
	# spawn a worker for msisdn-cli
	worker = pexpect.spawn("bash")
	worker.logfile = sys.stdout
	worker.expect("")
	print("bash spawned")
	worker.sendline("cd ./msisdn-cli")
	worker.sendline("make install")
	worker.expect("Successfully\sinstalled", timeout=10)
	worker.sendline("source .venv/bin/activate")
	print("venv activated")
	worker.sendline(cli_command)
	# worker = pexpect.spawn(cli_command)
	print("Executing command: " + cli_command)

	# retrieve the verification message
	print(worker.after)
	worker.expect("Please\senter\sthe\scode\sthat\syou\swill\sget\sby\sSMS\sfrom\s", timeout=10)
	print(worker.before)
	# print(worker.before)
	message_log = client.messages.list(gateway_number, test_number, time.strftime("%Y-%m-%d", time.gmtime()))
	while not message_log:
		time.sleep(1)
		message_log = client.messages.list(gateway_number, test_number, time.strftime("%Y-%m-%d", time.gmtime()))
	verification_message = message_log[0].body

	# extract the code
	match = re.search("^Your\sverification\scode\sis:\s(\d\d\d\d\d\d)", verification_message)
	worker.sendline(match.group(1))
	worker.expect("Verified")
	# print(worker.before)
	print("++++++++++++++++++++ Number: " + test_number + " VERIFIED +++++++++++++++++++")

def main():
	clean_up_message_logs()
	command = "msisdn-cli -H " + host + " -c " + mccs[0] + " -n " + numbers[0]
	run_msisdn_cli(command, host_number, numbers[0])


if __name__ == "__main__":
	main()