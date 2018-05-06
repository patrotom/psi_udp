#!/usr/bin/python3
import socket
import sys
from binascii import hexlify

BUFFER_SIZE = 512
SERVER_ADDRESS = '127.0.0.1', 4000
CHUNK = 255

class Error(Exception):
    pass
class ErrorClient(Error):
    pass
class ErrorServer(Error):
    pass

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
        tmp = int(str(hexlify(message[2]), 'utf-8'), base=16)
        print('ack=' + str(tmp), '', end=' ')
        print('flags=' + str(hexlify(message[3]), 'utf-8'), end=' ')
        print('data(' + str(len(message[4])) + '):', end=' ')
        if len(message[4]) > 1:
            for i in range(0, 8):
                print(hex(message[4][i])[2:].zfill(2), end=' ')
            print('...', end=' ')
            for i in range (len(message[4]) - 1, len(message[4]) - 9, -1):
                print(hex(message[4][i])[2:].zfill(2), end=' ')
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
            print('\nKilled by KeyboardInterrupt')

class Operation():
    '''Class from which will Download/Upload use common operations'''
    def __init__ (self, sock, controller):
        '''Constructor'''
        self.sock = sock
        self.controller = controller
        self.id = b''
        self.ack = 0
        self.ackChunks = []
        self.seqChunks = {}
        self.seq = 0
    
    def setup(self, type):
        '''Method which tells the probe that we are going to download a picture or upload a firmware'''
        sent = (0).to_bytes(8, 'big') + (4).to_bytes(1, 'big') + (type).to_bytes(1, 'big')
        to_print = (0).to_bytes(4, 'big'), (0).to_bytes(2, 'big'), (0).to_bytes(2, 'big'), (4).to_bytes(1, 'big'), (type).to_bytes(1, 'big')
        self.sock.settimeout(0.1)
        flag = True
        while True:
            flag = True
            self.controller.print(to_print, 'SEND')
            self.sock.sendto(sent, SERVER_ADDRESS)
            try:
                received = self.controller.receive()
                if int.from_bytes(received[3], 'big') != 4:
                    flag = False
            except socket.timeout:
                flag = False
            if flag == True:
                break

        self.id = received[0]
        self.controller.print(received, 'RECV')
        self.sock.settimeout(None)

class Download(Operation):
    '''Class which handles downloading of a picture from the probe'''
    def __init__(self, sock):
        '''Constructor'''
        super().__init__(sock, DatagramControl(sock))
        self.data = {}
        self.lastSeq = -1
        self.lastSize = -1

    def start(self):
        '''Method which starts and handles downloading'''
        try:
            super().setup(1)
            print('\n=========================================\nConnecton established, now downloading...\n=========================================\n')
            self.download()
        except ErrorClient:
            self.endError()
            print('====================================================\nConnection closed due to error on the client side...\n====================================================')
            return
        except ErrorServer:
            print('====================================================\nConnection closed due to error on the server side...\n====================================================')
            self.sock.close()
            return
        self.endConnection()

    def endError(self):
        '''Method which sends rst flag and ends connection due to error'''
        sent = self.id + (0).to_bytes(2, 'big') + self.ack.to_bytes(2, 'big') + (1).to_bytes(1, 'big')
        to_print = self.id, (0).to_bytes(2, 'big'), self.ack.to_bytes(2, 'big'), (1).to_bytes(1, 'big'), []
        self.sock.sendto(sent, SERVER_ADDRESS)
        self.controller.print(to_print, 'SEND')
        self.sock.close()

    def endConnection(self):
        '''Method which ends connection regularly and send fin flag'''
        sent = self.id + (0).to_bytes(2, 'big') + self.ack.to_bytes(2, 'big') + (2).to_bytes(1, 'big')
        to_print = self.id, (0).to_bytes(2, 'big'), self.ack.to_bytes(2, 'big'), (2).to_bytes(1, 'big'), []
        self.sock.sendto(sent, SERVER_ADDRESS)
        self.controller.print(to_print, 'SEND')
        
        self.sock.close()
        print('=================================================================\nSuccess: Connection was closed. Transferred', self.ack, 'bytes','\n=================================================================')

    def download(self):
        '''Method which downloads data from the probe'''
        while True:
            received = self.controller.receive()
            self.controller.print(received, 'RECV')

            if int.from_bytes(received[3], 'big') == 2:
                break
            if int.from_bytes(received[3], 'big') == 1:
                raise ErrorServer
            if received[0] != self.id:
                raise ErrorClient
            
            if self.ackChunks.count(int.from_bytes(received[1], 'big')) == 0:
                self.seqChunks[int.from_bytes(received[1], 'big')] = 1
                self.ackChunks.append(int.from_bytes(received[1], 'big'))
                self.data[int.from_bytes(received[1], 'big')] = received[4]
                if len(received[4]) != 255:
                    self.lastSeq = int.from_bytes(received[1], 'big')
                    self.lastSize = len(received[4])
                if (self.ack % 65536) == int.from_bytes(received[1], 'big'):
                    if len(received[4]) == 255:
                        self.ack = (self.ack + CHUNK) % 65536
                    else:
                        self.ack = (self.ack + len(received[4])) % 65536
            else:
                self.seqChunks[int.from_bytes(received[1], 'big')] += 1
                if self.seqChunks[int.from_bytes(received[1], 'big')] == 20:
                    raise ErrorClient
            
            while True:
                if self.ackChunks.count(self.ack % 65536) == 0:
                    break
                if self.lastSeq != self.ack:
                    self.ack = (self.ack + CHUNK) % 65536
                else:
                    self.ack = (self.ack + self.lastSize) % 65536

            sent = self.id + (0).to_bytes(2, 'big') + self.ack.to_bytes(2, 'big') + (0).to_bytes(1, 'big')
            to_print = self.id, (0).to_bytes(2, 'big'), self.ack.to_bytes(2, 'big'), (0).to_bytes(1, 'big'), []
            self.sock.sendto(sent, SERVER_ADDRESS)
            self.controller.print(to_print, 'SEND')
    
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
