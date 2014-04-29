#!/usr/bin/python

import xml.etree.ElementTree as ET

class Device:
	"""A class to represent Insteon Devices from a saved xml file."""

	def __init__(self, filename):
		tree = ET.parse(filename)
		root = tree.getroot() 
		self.devicesByRoomAndName = {}
		self.devicesByName = {}
		for device in root.findall("./insteon/active_devices/device"):
			location=device.find('location')
			self.devicesByName[device.get("displayName")]=device.get("insteonID")
			self.devicesByRoomAndName["{0} - {1}".format(location.get("room"), device.get("displayName"))]=device.get("insteonID")
			print "{0} - {1}".format(location.get("room"), device.get("displayName"))

	def howmany(self):
		print "Number of devices by name {0}".format(len(self.devicesByName))
		print "Number of devices by room and name {0}".format(len(self.devicesByRoomAndName))

	def getDeviceByName(self, displayName):
		return self.devicesByName[displayName]

	def getDeviceByRoomAndName(self, roomAndDisplayName):
		return self.devicesByRoomAndName[roomAndDisplayName]

	def getDevice(self, name):
		deviceId=self.devicesByRoomAndName[name]
		if deviceId is None:
			deviceId=self.devicesByName[name]
		return deviceId
