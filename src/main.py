#!/usr/bin/python3
import socket
import sys

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    while True:
        print('\nwaiting to receive message')
        data, address = sock.recvfrom(4096)

        print('Received: ', data.decode('ascii'))

        if data:
            sock.sendto('data received'.encode(), address)

main ()
