#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os, sys
from subprocess import Popen, PIPE, STDOUT

cmd1 = "source ../../msisdn-cli/.venv/bin/activate"
cmd2 = "msisdn-cli -H https://msisdn.services.mozilla.com -c 310"
child_process = subprocess.Popen("{}; {}".format(cmd1, cmd2), stdin=PIPE, stdout=None, stderr=None, shell=True)
child_process.communicate("+16507399259")


