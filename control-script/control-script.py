#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os, sys
from subprocess import Popen, PIPE, STDOUT

import pexpect

virtualenv_command = "source ../../msisdn-cli/.venv/bin/activate"
worker_host = "msisdn-cli -H https://msisdn.services.mozilla.com"
# child_process = subprocess.Popen("{}; {}".format(cmd1, cmd2), stdin=PIPE, stdout=None, stderr=None, shell=True)
# child_process.communicate("+16507399259")

# spawn a worker for msisdn-cli
worker = pexpect.spawn("bash")
worker.sendline(virtualenv_command)
print worker.before
worker.expect("")
print "Entered virtualenv"
print worker.before
msisdn_command = worker_host + " -c 310 -n +16507399259"
print msisdn_command
print worker.before
worker.sendline(msisdn_command)
print "msisdn_command sent"
print worker.before
worker.expect("Please\senter\sthe\scode\sthat", timeout=4)
print "Code sent"
worker.interact()

