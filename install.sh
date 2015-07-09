#!/bin/sh
virtualenv venv
source venv/bin/activate
python ./setup.py develop
