#!/bin/sh
virtualenv venv
. venv/bin/activate
python ./setup.py develop
