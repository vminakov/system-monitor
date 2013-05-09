#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       stop_servers.py
#       
#		A simple script to stop WebScoket server instances


import subprocess, os, signal, sys

grepRegex = 'server_info\.py\|server_process\.py\|server_memory\.py\|server_cpu\.py\|server_network\.py'
#output = subprocess.call('ps aux | grep "%s"' % (grepRegex), shell=True)

p1 = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", grepRegex], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output = p2.communicate()[0]

print output

if len(output) == 0:
	print("No running server intances found. Exiting.")
	sys.exit()

grepLines = output.split('\n')

pids = []
for line in grepLines:
	if len(line) > 0:
		pids.append(int(line.split()[1]))

print("Killing processes: %s" % (pids))
for pid in pids:
	os.kill(pid, signal.SIGKILL)
