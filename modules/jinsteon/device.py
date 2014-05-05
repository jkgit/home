#!/usr/bin/python

import os
import requests
import xml.etree.ElementTree as ET

class Device:
	"""A class to represent Insteon Devices from a saved xml file."""
	devicesByRoomAndName = None
	devicesByName = None
	devicesTwoDimensional = None
	devicesByInsteonID = None

	def __init__(self, insteonID, room, name, element):
		self.insteonID=insteonID
		self.room=room
		self.name=name
		self.element=element

	def turnOn(self):
		url = 'http://192.168.0.50:25105/3?0262{0}0F11FF=I=3'.format(self.insteonID.replace(".",""))
		r = requests.post(url)
		return url

	def turnOff(self):
		url = 'http://192.168.0.50:25105/3?0262{0}0F1300=I=3'.format(self.insteonID.replace(".",""))
		r = requests.post(url)
		return url

	@classmethod
	def get(cls, insteonID):
		loadAll(cls)
		return devicesByInsteonID[insteonID]

	@classmethod
	def loadAll(cls, devicePath):
		print "Loading all devices from {0}".format(devicePath)
		if cls.devicesByName is None:
			tree = ET.parse(devicePath)
			root = tree.getroot() 
			cls.devicesByRoomAndName = {}
			cls.devicesByName = {}
			cls.devicesTwoDimensional = {}
			cls.devicesByInsteonID = {}

			for deviceElement in root.findall("./insteon/active_devices/device"):
				wattage=deviceElement.get("wattage")
				# a wattage of -1 means it does not have a connected load so skip it
				if wattage!="-1":
					location=deviceElement.find('location')
					room=location.get("room")
					name=deviceElement.get("displayName")
					insteonID=deviceElement.get("insteonID")

					device = cls(insteonID, room, name, deviceElement)

					cls.devicesByName[name]=device
					cls.devicesByRoomAndName["{0} - {1}".format(room, name)]=device
					if not cls.devicesTwoDimensional.has_key(room):
						cls.devicesTwoDimensional[room]={}
					cls.devicesTwoDimensional[room][name]=device 
					cls.devicesByInsteonID[insteonID]=device
					print "{0} - {1}".format(room, name)
		return cls

	
	@staticmethod
	def howmany():
		print "Number of devices by name {0}".format(len(Device.devicesByName))
		print "Number of devices by room and name {0}".format(len(Device.devicesByRoomAndName))
		print "Number of rooms {0}".format(len(Device.devicesTwoDimensional))

	@staticmethod
	def getDeviceByInsteonID(insteonID):
		return Device.devicesByInsteonID[insteonID]

	@staticmethod
	def getDeviceByName(displayName):
		return Device.devicesByName[displayName]

	@staticmethod
	def getDeviceByRoomAndName(roomAndDisplayName):
		return Device.devicesByRoomAndName[roomAndDisplayName]

	@staticmethod
	def getDevice(name):
		device=Device.devicesByRoomAndName[name]
		if device is None:
			device=Device.devicesByName[name]
		return deviceId
