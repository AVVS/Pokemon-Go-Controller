#!/usr/bin/env python
import os
import urllib2
import json
import time
import sys
import signal
import random

ip = "http://192.168.1.3:8080/"

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

def id_generator(size=1, chars="\\|/"):
   return ''.join(random.choice(chars) for _ in range(size))

def clickAction():
	os.system("./autoClicker -x 505 -y 1049")
	time.sleep(0.1)
	os.system("./autoClicker -x 544 -y 1103")
	time.sleep(1)
	print id_generator(), "clicking!!              \r",
	sys.stdout.flush()

def start():
	while True:
		if checkConnected() != None:
			clickAction()

signal.signal(signal.SIGINT, signal_handler)

start()
