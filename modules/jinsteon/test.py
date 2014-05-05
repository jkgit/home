#!/usr/bin/python

import time
from device import Device

Device.loadAll("../../private/devices.xml")
Device.howmany()
device=Device.getDeviceByRoomAndName("Kitchen - Lights")
print "{1} id {0}".format(device.insteonID, device.name)
device.turnOn()
time.sleep(5)
device.turnOff()

