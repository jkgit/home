#!/usr/bin/python

import Device

device=Device("devices.xml")
device.howmany()
print "Dork nook track light id {0}".format(device.getDeviceByRoomAndName("Dork Nook - Track Lights"))
