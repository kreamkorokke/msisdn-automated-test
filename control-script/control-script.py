#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect
import time
import re
from twilio.rest import TwilioRestClient

worker_host = "msisdn-cli -H https://msisdn.services.mozilla.com"
account_sid = "ACea6b158b0109812803f02e90e026fa0c"
auth_token = "b6c0cf4ac5b0c28b681a490b16f352a2"
client = TwilioRestClient(account_sid, auth_token)

# clean up the previous message logs
messages = client.messages.list()
for i in range(0, len(messages)):
	client.messages.delete(messages[i].sid)

# spawn a worker for msisdn-cli
msisdn_command = worker_host + " -c 310 -n +16502650808"
worker = pexpect.spawn(msisdn_command)
print("Executing command: " + msisdn_command)

# retrieve the verification message
worker.expect("Please\senter\sthe\scode\sthat")
message_log = client.messages.list("+12182967993", "+16502650808", time.strftime("%Y-%m-%d", time.gmtime()))
while not message_log:
	time.sleep(1)
	message_log = client.messages.list("+12182967993", "+16502650808", time.strftime("%Y-%m-%d", time.gmtime()))
verification_message = message_log[0].body

# extract the code
match = re.search("^Your\sverification\scode\sis:\s(\d\d\d\d\d\d)", verification_message)
# worker.sendline(match.group(1))
worker.sendline("111111")