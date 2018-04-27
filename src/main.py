#!/usr/bin/python3
import socket
import sys
from binascii import hexlify

BUFFER_SIZE = 512
SERVER_ADDRESS = '127.0.0.1', 4000

class DatagramControl():
    '''Class which receives messages'''
    def __init__(self, sock):
        '''Cosntructor'''
        self.sock = sock
        self.address = None
    
    def getDatagram(self):
        '''Method which will receive a new datagram'''
        data = self.sock.recvfrom(BUFFER_SIZE)[0]
        return data
    
    def receive(self):
        '''Method which will parse a datagram and return tuple'''
        data = self.getDatagram()
        # (0,4)-ID, (4,6)-seq, (6,8)-ack, (8,9)-flags, (9,END)-data
        return data[0:4], data[4:6], data[6:8], data[8:9], data[9:]

    def send(self, message):
        '''Method which will send a datagram'''
        self.sock.sendto(message.encode(), SERVER_ADDRESS)
    
    def print(self, message, type):
        '''Method which prints datagram'''
        print(str(hexlify(message[0]), 'utf-8') + ' ' + type, '', end=' ')
        tmp = int(str(hexlify(message[1]), 'utf-8'), base=16)
        print('seq=' + str(tmp), '', end=' ')
        tmp = int(str(hexlify(message[1]), 'utf-8'), base=16)
        print('ack=' + str(tmp), '', end=' ')
        print('flags=' + str(hexlify(message[3]), 'utf-8'), end=' ')
        print('data(' + str(len(message[4])) + '):', end=' ')
        if len(message[4]) > 1:
            for i in range(0, 8):
                print(hex(message[4][i])[2:], end=' ')
            print('...', end=' ')
            for i in range (len(message[4]) - 1, len(message[4]) - 9, -1):
                print(hex(message[4][i])[2:], end=' ')
        elif len(message[4]) == 1:
            print(str(hexlify(message[4]), 'utf-8'), end='')
        else:
            print('-')
        print('')

class Handler():
    '''Class which handles received messages'''
    def __init__(self, sock):
        '''Constructor'''
        self.sock = sock
        self.controler = DatagramControl(sock)

    def handle(self, operation):
        '''Method which handles required operation (0-download, 1-upload)'''
        try:
            if operation == 2:
                u = Upload(self.sock)
                u.start()
            else:
                d = Download(self.sock)
                d.start()
        except KeyboardInterrupt:
            print('Killed by KeyboardInterrupt')

class Operation():
    '''Class from which will Download/Upload use common operations'''
    def __init__ (self, sock, controller):
        '''Constructor'''
        self.sock = sock
        self.controller = controller
        self.id = b''
    
    def setup(self, type):
        '''Method which tells the probe that we are going to download a picture or upload a firmware'''
        sent = (0).to_bytes(8, 'big') + (4).to_bytes(1, 'big') + (type).to_bytes(1, 'big')
        to_print = (0).to_bytes(4, 'big'), (0).to_bytes(2, 'big'), (0).to_bytes(2, 'big'), (4).to_bytes(1, 'big'), (type).to_bytes(1, 'big')
        self.controller.print(to_print, 'SEND')
        self.sock.sendto(sent, SERVER_ADDRESS)
        received = self.controller.receive()
        self.controller.print(received, 'RECV')

class Download(Operation):
    '''Class which handles downloading of a picture from the probe'''
    def __init__(self, sock):
        '''Constructor'''
        super().__init__(sock, DatagramControl(sock))

    def start(self):
        '''Method which starts and handles downloading'''
        super().setup(1)
    
class Upload(Operation):
    '''Class which handles uploading of a firmware to the probe'''
    def __init__(self, sock):
        '''Constructor'''
        super().__init__(sock, DatagramControl(sock))
    
    def start(self):
        '''Method which starts and handles uploading'''

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 10000)
    print('Starting up on {}, port {}\n'.format(*server_address))
    sock.bind(server_address)
    h = Handler(sock)
    h.handle(1)
    
main ()
