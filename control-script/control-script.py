#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect

worker_host = "msisdn-cli -H https://msisdn.services.mozilla.com"

# spawn a worker for msisdn-cli
msisdn_command = worker_host + " -c 310 -n +16507399259"
worker = pexpect.spawn(msisdn_command)
print("Executing command: " + msisdn_command)
worker.expect("Please\senter\sthe\scode\sthat")
worker.interact()