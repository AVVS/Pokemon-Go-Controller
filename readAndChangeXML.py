#!/usr/bin/env python
import xml.etree.cElementTree as ET
import urllib2
import json
import time
import sys
import random
import signal

ip = "http://192.168.1.3:8080/"
lastLat = ""
lastLng = ""

def id_generator(size=1, chars="\\|/"):
   return ''.join(random.choice(chars) for _ in range(size))

def signal_handler(signal, frame):
    print('\nClosing app!')
    sys.exit(0)

def getPokemonLocation():
	try:
		response = urllib2.urlopen(ip, timeout = 1)
		return json.load(response)
	except urllib2.URLError as e:
		print id_generator(), "Error:", e.reason, "                                                                     \r",
		sys.stdout.flush()
		time.sleep(1)

def generateXML():
	global lastLat, lastLng
	geo = getPokemonLocation()
	if geo != None:
		if geo["lat"] != lastLat or geo["lng"] != lastLng:
			lastLat = geo["lat"]
			lastLng = geo["lng"]
			gpx = ET.Element("gpx", version="1.1", creator="Xcode")
			wpt = ET.SubElement(gpx, "wpt", lat=geo["lat"], lon=geo["lng"])
			ET.SubElement(wpt, "name").text = "PokemonLocation"
			ET.ElementTree(gpx).write("pokemonLocation.gpx")
			print id_generator(), "Location Updated!", "latitude:", geo["lat"], "longitude:" ,geo["lng"], "\r",
			sys.stdout.flush()

def start():
	while True:
		generateXML()

signal.signal(signal.SIGINT, signal_handler)

start()
