#!/usr/bin/env python

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

REQUIREMENTS = [
    'fabric',
    'twilio',
    'pexpect',
    'setuptools',
    'six',
    'docopt',
    'requests==2.7.0',
    'requests-hawk',
    'PyBrowserID'
]

setup(
    name='msisdn-automated-test',
    version='1.0.0',
    description='msisdn-automated-test',
    long_description=README,
    author='Koki Yoshida',
    author_email='kreamkorokke@gmail.com',
    url='https://github.com/kreamkorokke/msisdn-automated-test',
    license="MIT",
    install_requires=REQUIREMENTS,
    keywords=['msisdn-automated-test', 'setup.py'],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],

)