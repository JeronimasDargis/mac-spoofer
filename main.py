#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:23:12", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)