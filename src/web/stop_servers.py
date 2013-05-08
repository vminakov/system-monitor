#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       stop_servers.py
#       
#		A simple script to stop WebScoket server instances


import subprocess, os, signal

grepRegex = 'server_info\.py\|server_process\.py\|server_memory\.py\|server_cpu\.py\|server_network\.py'
grepLines = subprocess.check_output('ps aux | grep "%s"' % (grepRegex), shell=True).split('\n')

pids = []
for line in grepLines:
	if len(line) > 0:
		pids.append(int(line.split()[1]))

print("Killing processes: %s" % (pids))
for pid in pids:
	os.kill(pid, signal.SIGKILL)
