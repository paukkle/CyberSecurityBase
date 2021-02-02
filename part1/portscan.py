#!/usr/bin/env python3
import sys
import socket


def get_accessible_ports(address, min_port, max_port):
    found_ports = []

    for port_n in range(min_port, max_port + 1):
        s = socket.socket()
        try:
            s.connect((address, port_n))
            data = s.recv(1024)
            found_ports.append(data)

        except:
            pass
    return found_ports


def main():
	address = "127.0.0.1"
	min_port = 20050
	max_port = 20150
	ports = get_accessible_ports(address, min_port, max_port)
	for p in ports:
		print(p)


main()
