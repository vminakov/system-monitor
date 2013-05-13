#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       start_servers.py
#       
#		A primitive script to start WebSocket servers.

import subprocess

subprocess.Popen(['python', 'server_info.py'])
subprocess.Popen(['python', 'server_process.py'])
subprocess.Popen(['python', 'server_memory.py'])
subprocess.Popen(['python', 'server_cpu.py'])
subprocess.Popen(['python', 'server_network.py'])
subprocess.Popen(['python', 'server_log.py'])
