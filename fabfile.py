from fabric.api import *
import fabric

@task
def setup():
    local("git clone https://github.com/kreamkorokke/msisdn-cli")
    # with fabric.context_managers.lcd("./msisdn-cli"):
    # 	local("sudo make install")

@task
def teardown():
    # with fabric.context_managers.lcd("./msisdn-cli"):
	   #  local("sudo make clean")
    local("rm -fr ./msisdn-cli")
