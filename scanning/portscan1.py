#!/usr/bin/python

import socket

print("Welcome to simple port scanner!")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Enter the IP address: ")
port = int(input("Enter the port: "))

def portscanner(port):
	if sock.connect_ex((host, port)):
		print("Port {} is closed".format(port))
	else:
		print("Port {} is opened".format(port))

portscanner(port)

