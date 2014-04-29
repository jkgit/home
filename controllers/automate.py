# coding: utf8
import eiscp
import socket
import serial
import time
import requests
from jinsteon import Device
import os

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    in this case it isn't really very useful since we could just call the actual service funtion,
    but if there are ever any services that return useful data in different formats it may be good practice.
    """
    return service()

@service.run
def wallUp():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto("UP", ("localhost",5000))
    return "success"

@service.run
def wallDown():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto("DOWN", ("localhost",5000))
    return "success"

@service.run
def goodnight():
    turnOffAudio()
    turnOffProjector()
    turnOnLights()
    return "success"

@service.run
def watchComputer():
    turnOnAudio("Computer/PC")
    turnOnProjector("Input A")
    turnOffLights()
    return "success"

@service.run
def watchDirectv():
    turnOnAudio("VIDEO2    CBL/SAT")
    turnOnProjector("Component")
    turnOffLights()
    return "success"

def getSerialConnection():
    return serial.Serial("/dev/ttyUSB0", 38400, timeout=1, parity=serial.PARITY_EVEN)

def turnOnProjector(source):
    ser = getSerialConnection()
    ser.write("\xa9\x17\x2e\x00\x00\x00\x3f\x9a\n")
    time.sleep(0.5)
    if source=='Input A':
        ser.write("\xa9\x17\x2b\x00\x00\x00\x3f\x9a\n")
    elif source=='Component':
        ser.write("\xa9\x17\x2c\x00\x00\x00\x3f\x9a\n")

def turnOffProjector():
    ser = getSerialConnection()
    ser.write("\xa9\x17\x2f\x00\x00\x00\x3f\x9a\n")

def turnOnAudio(source):
    # Create a receiver object attached to the host 192.168.0.40
    receiver = eiscp.eISCP('192.168.0.40')
    receiver.writeCommandFromName('Power ON')
    time.sleep(0.1)
    receiver.writeCommandFromName(source)

def turnOffAudio():
    # Create a receiver object attached to the host 192.168.0.40
    receiver = eiscp.eISCP('192.168.0.40')
    receiver.writeCommandFromName('Power OFF')
    
def turnOffLights():
    devicePath = os.path.join(request.folder, 'private', 'devices.xml')
    deviceId = Device(devicePath).getDeviceByRoomAndName("Movie - Lights").translate(None, '.')
    r = requests.get('http://192.168.0.50:25105/3?0262{0}0F13FF=I=3-'.format(deviceId))
    r.status_code

def turnOnLights():
    devicePath = os.path.join(request.folder, 'private', 'devices.xml')
    deviceId = Device(devicePath).getDeviceByRoomAndName("Movie - Lights").translate(None, '.')
    r = requests.get('http://192.168.0.50:25105/3?0262{0}0F11FF=I=3-'.format(deviceId))
    r.status_code
