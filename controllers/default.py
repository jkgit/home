# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import eiscp
import os
from jinsteon import Device

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to Home Automator!")
    return dict(message=T('Home Automator'))

def devices():
    response.flash = T("All Insteon Devices")
    return dict(message=T('All Insteon Devices By Name'),devices=Device.devicesTwoDimensional)

def initialize():
    devicePath = os.path.join('applications', 'home', 'private', 'devices.xml')
    with open("log.txt", "a") as f:
	f.write(devicePath)
	f.write(os.getcwd())
    Device.loadAll(devicePath)
