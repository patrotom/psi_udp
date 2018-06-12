#!/usr/bin/python3
import socket
import sys
import os
from binascii import hexlify
from sortedcontainers import SortedDict

BUFFER_SIZE = 512
SERVER_PORT = 4000
CLIENT_PORT = 10000
CLIENT_ADDRESS = 'localhost'
SERVER_ADDRESS = '127.0.0.1', SERVER_PORT
FIRMWARE = 'firmware.bin'
CHUNK = 255
MOD = 65536
WINDOW_SIZE = 2040


class Error(Exception):
    '''Default Exception class'''
    pass
class ErrorServer(Error):
    '''Error on the server side Exception'''
    pass
class ErrorClient(Error):
    '''Error on the client side Exception'''
    pass


class DatagramControl():
    '''Class which receives messages'''
    def __init__(self, sock):
        '''Cosntructor'''
        self.sock = sock
        self.address = None
    
    def get_datagram(self):
        '''Method which will receive a new datagram'''
        data = self.sock.recvfrom(BUFFER_SIZE)[0]
        return data
    
    def receive(self):
        '''Method which will parse a datagram and return tuple'''
        data = self.get_datagram()
        # (0,4)-ID, (4,6)-seq, (6,8)-ack, (8,9)-flags, (9,END)-data
        return data[0:4], data[4:6], data[6:8], data[8:9], data[9:]

    def send(self, message):
        '''Method which will send a datagram'''
        self.sock.sendto(message.encode(), SERVER_ADDRESS)
    
    def print(self, message, type):
        '''Method which prints datagram'''
        print(str(hexlify(message[0]), 'utf-8').upper() + ' ' + type, '', end=' ')
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
    '''Class which handles types of the operations'''
    def __init__(self, sock):
        '''Constructor'''
        self.sock = sock
        self.controler = DatagramControl(sock)

    def handle(self, operation):
        '''Method which handles required operation (0-download, 1-upload)'''
        try:
            if operation == 2:
                # Ready for implementation of upload
                pass
            elif operation == 1:
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
        self.last_data = b''
        self.ack = 0
        self.ack_chunks = []
        self.mod_list = []
        self.seq_chunks = {}
        self.data = {}
    
    def setup(self, type):
        '''Method which tells the probe that we are going to download a picture or upload a firmware'''
        sent = (0).to_bytes(8, 'big') + (4).to_bytes(1, 'big') + (type).to_bytes(1, 'big')
        to_print = (0).to_bytes(4, 'big'), (0).to_bytes(2, 'big'), (0).to_bytes(2, 'big'), (4).to_bytes(1, 'big'), (type).to_bytes(1, 'big')
        self.sock.settimeout(0.1)
        
        flag = True
        cnt = 0
        while True:
            flag = True
            self.controller.print(to_print, 'SEND')
            self.sock.sendto(sent, SERVER_ADDRESS)
            try:
                if cnt == 20:
                    raise ErrorClient
                received = self.controller.receive()
                self.id = received[0]
                self.controller.print(received, 'RECV')
                if int.from_bytes(received[3], 'big') != 4:
                    flag = False
                elif int.from_bytes(received[3], 'big') == 0:
                    raise ErrorServer
            except socket.timeout:
                flag = False
            if flag == True:
                break
            cnt += 1
        
        if len(received[4]) != 1 and (int.from_bytes(received[4], 'big') != 1 or int.from_bytes(received[4], 'big') != 2):
            raise ErrorClient
        self.sock.settimeout(None)
    
    def end_error(self):
        '''Method which sends rst flag and ends connection due to detected error on the client side'''
        sent = self.id + (0).to_bytes(2, 'big') + self.ack.to_bytes(2, 'big') + (1).to_bytes(1, 'big')
        to_print = self.id, (0).to_bytes(2, 'big'), self.ack.to_bytes(2, 'big'), (1).to_bytes(1, 'big'), []
        self.sock.sendto(sent, SERVER_ADDRESS)
        self.controller.print(to_print, 'SEND')
        self.sock.close()

    def end_connection(self):
        '''Method which ends connection regularly and send fin flag'''
        sent = self.id + (0).to_bytes(2, 'big') + self.ack.to_bytes(2, 'big') + (2).to_bytes(1, 'big')
        to_print = self.id, (0).to_bytes(2, 'big'), self.ack.to_bytes(2, 'big'), (2).to_bytes(1, 'big'), []
        self.sock.sendto(sent, SERVER_ADDRESS)
        self.controller.print(to_print, 'SEND')
        self.sock.close()
        print('======================================================\nSuccess: Connection was closed. All bytes transferred.\n======================================================')
        self.write_photo_to_file()

    def write_photo_to_file(self):
        '''Method which writes bytes to file and creates a valid photograph'''
        f_download = open('tmp/transferred.png', 'wb')
        for i in self.mod_list:
            data_keys = list(self.data[i].keys())
            for j in data_keys:
                f_download.write(self.data[i][j])
        f_download.write(self.last_data)
        f_download.close()


class Download(Operation):
    '''Class which handles downloading of a picture from the probe'''
    def __init__(self, sock):
        '''Constructor'''
        super().__init__(sock, DatagramControl(sock))
        self.last_seq = -1
        self.last_size = -1

    def start(self):
        '''Method which starts and handles downloading'''
        try:
            super().setup(1)
            print('\n=========================================\nConnecton established, now downloading...\n=========================================\n')
            self.download()
            super().end_connection()
        except ErrorServer:
            print('=====================================================\nError detected on the server side, connection closed.\n=====================================================')
            self.sock.close()
        except ErrorClient:
            super().end_error()
            print('=====================================================\nError detected on the client side, connection closed.\n=====================================================')
            self.sock.close()

    def download(self):
        '''Method which downloads data from the probe'''
        while True:
            received = self.controller.receive()
            self.controller.print(received, 'RECV')
            
            if self.validate_input(received):
                break
            self.ack_count(received)

            sent = self.id + (0).to_bytes(2, 'big') + self.ack.to_bytes(2, 'big') + (0).to_bytes(1, 'big')
            to_print = self.id, (0).to_bytes(2, 'big'), self.ack.to_bytes(2, 'big'), (0).to_bytes(1, 'big'), []
            self.sock.sendto(sent, SERVER_ADDRESS)
            self.controller.print(to_print, 'SEND')
    
    def ack_count(self, received):
        '''Method which calculates desired ack'''
        if self.ack_chunks.count(int.from_bytes(received[1], 'big')) == 0:
            self.seq_chunks[int.from_bytes(received[1], 'big')] = 1
            self.ack_chunks.append(int.from_bytes(received[1], 'big'))
            
            self.update_data(received)

            if len(received[4]) != CHUNK:
                self.last_seq = int.from_bytes(received[1], 'big')
                self.last_size = len(received[4])
                self.last_data = received[4]
            if (self.ack % MOD) == int.from_bytes(received[1], 'big'):
                if len(received[4]) == CHUNK:
                    self.ack = (self.ack + CHUNK) % MOD
                else:
                    self.ack = (self.ack + len(received[4])) % MOD
        else:
            self.seq_chunks[int.from_bytes(received[1], 'big')] += 1
            if self.seq_chunks[int.from_bytes(received[1], 'big')] == 20:
                raise ErrorServer

        while True:
            if self.ack_chunks.count(self.ack % MOD) == 0:
                break
            if self.last_seq != self.ack:
                self.ack = (self.ack + CHUNK) % MOD
            else:
                self.ack = (self.ack + self.last_size) % MOD

    def update_data(self, received):
        '''Method which handles correct storing of downloaded data'''
        if len(received[4]) == CHUNK:
            idx = int.from_bytes(received[1], 'big') % CHUNK
            if idx == 0:
                idx = CHUNK
            if self.mod_list.count(idx) == 0:
                self.data[idx] = SortedDict({})
                self.mod_list.append(idx)
            self.data[idx][int.from_bytes(received[1], 'big')] = received[4]

    def validate_input(self, received):
        '''Method which validates input data'''
        if int.from_bytes(received[3], 'big') == 2:
            if len(received[4]) != 0:
                raise ErrorClient
            return True
        if int.from_bytes(received[3], 'big') == 1:
            raise ErrorServer
        if int.from_bytes(received[3], 'big') != 0:
            raise ErrorClient
        if received[0] != self.id:
            raise ErrorClient
        return False


def parse_args():
    '''Function which parses input arguments'''
    global SERVER_ADDRESS
    global FIRMWARE
    if len(sys.argv) == 2:
        SERVER_ADDRESS = sys.argv[1], SERVER_PORT
        return 1
    elif len(sys.argv) == 3:
        SERVER_ADDRESS = sys.argv[1], SERVER_PORT
        FIRMWARE = sys.argv[2]
        return 2
    else:
        print('Usage: ./main.py <server> (<firmware.bin> - only for upload)')


def main():
    '''Main of this program'''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (CLIENT_ADDRESS, CLIENT_PORT)
    print('Starting up on {}, port {}\n'.format(*server_address))
    sock.bind(server_address)
    h = Handler(sock)
    h.handle(parse_args())

main ()
