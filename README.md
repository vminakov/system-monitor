system-monitor
==============

To run both web and GUI applications following
packages must be installed (instructions for ubuntu 12.04>= and debian 7.0):


1. Install Qt and Pyside
	sudo apt-get install pyside

2. Install Twisted with autobahn from PIP
	sudo apt-get intsall pip
	sudo pip install autobahn
	sudo pip install psutil

3. To launch the GUI application:
	gksudo src/system_monitor.py

4. To launch websocket servers
	sudo src/web/start_servers.py

5. To stop websocket servers
	sudo src/web/stop_servers.py
