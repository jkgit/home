import os
from jinsteon import Device

devicePath = os.path.join(os.getcwd(), 'applications', 'home', 'private', 'devices.xml')
print devicePath
print os.getcwd()
Device.loadAll(devicePath)
print "devices loaded"
