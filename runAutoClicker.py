#!/usr/bin/env python
import os
import urllib2
import json
import time
import sys
import signal
import random
import socket

ip = "http://192.168.5.42:8080/"

def signal_handler(signal, frame):
    print('\nClosing app!')
    sys.exit(0)

def checkConnected():
	try:
		response = urllib2.urlopen(ip, timeout = 1)
		return json.load(response)
	except urllib2.URLError as e:
		print id_generator(), "Error:", e.reason, "                            \r",
		sys.stdout.flush()
		time.sleep(1)
	except socket.timeout:
		print id_generator(), "Timeout error                                   \r",
		sys.stdout.flush()
		time.sleep(1)

def id_generator(size=1, chars="\\|/"):
   return ''.join(random.choice(chars) for _ in range(size))

def clickAction():
	os.system("cliclick -m verbose -r c:505,1183 w:100 c:+50,-283")
	time.sleep(1)

def start():
	while True:
		if checkConnected() != None:
			clickAction()

signal.signal(signal.SIGINT, signal_handler)

start()
