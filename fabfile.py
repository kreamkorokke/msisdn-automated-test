from fabric.api import local
import fabric

def setup():
    local("git clone https://github.com/kreamkorokke/msisdn-cli")
    with fabric.context_managers.lcd("./msisdn-cli"):
    	local("make install")

def teardown():
    with fabric.context_managers.lcd("./msisdn-cli"):
	    local("make clean")
    local("rm -fr ./msisdn-cli")
