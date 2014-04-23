# coding: utf8
import eiscp
import socket

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

"""


# Turn the receiver on
#receiver.writeCommandFromName('Power ON')

# Select the PC input
#receiver.writeCommandFromName('Computer/PC')
#receiver.writeCommandFromName('TUNER')

# Done watching a movie, shut it off.
receiver.writeCommandFromName('Power OFF')
"""

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
    # Create a receiver object attached to the host 192.168.1.124
#    receiver = eiscp.eISCP('192.168.0.40')
#    receiver.writeCommandFromName('Power OFF')
    return "success"

@service.run
def watchMovie():
    # Create a receiver object attached to the host 192.168.1.124
#    receiver = eiscp.eISCP('192.168.0.40')
#    receiver.writeCommandFromName('Power ON')
#    receiver.writeCommandFromName('Computer/PC')
    """
    Turn on projector
    Turn off lights
    """
    return "success"
