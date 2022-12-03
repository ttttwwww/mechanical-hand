import threading
import socket
from PyQt5.QtCore import QThread, pyqtSignal

import setting


class NetWork(QThread):
    tcp_client_connected = pyqtSignal(tuple)
    def __init__(self):
        super(NetWork, self).__init__()
        self.message = None
        self.server_address = setting.net_address
        self.port = setting.net_port
        self.id_client = 0
        self.clients=[]

    def set_address(self,address):
        self.server_address = address
    def set_port(self,port):
        self.server_port = port
    def tcp_server_setup(self):
        self.tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.tcp_server.bind((self.server_address, self.server_port))
        self.tcp_server.listen(128)
    def send(self,message):
        self.clients[self.id_client].load_message(message)

    def run(self):
        while True:
            client, client_address = self.tcp_server.accept()
            print("client connected")
            print(client_address)
            client = ClientThread(client,client_address[0],client_address[1])
            client.start()
            self.clients.append(client)
            self.tcp_client_connected.emit(client_address)
            # while True:
            #     recv_data = self.client.recv(4096)
            #     # 6 有消息就回复数据，消息长度为0就是说明客户端下线了
            #     if recv_data:
            #         print("客户端是:", self.client_address)
            #         print("客户端发来的消息是:", recv_data.decode())
            #     if self.message != None:
            #         self.tcp_server.send(self.message)
            #         self.message = None

class ClientThread(QThread):
    def __init__(self,client,address,port):
        super(ClientThread, self).__init__()
        self.address = address
        self.port = port
        self.client = client
        self.message = None
    def load_message(self,message):
        self.message = message

    def run(self):
        while True:
            recv_data = self.client.recv(4096)
            # 6 有消息就回复数据，消息长度为0就是说明客户端下线了
            if recv_data:
                print("客户端是:", self.address,self.port)
                print("客户端发来的消息是:", recv_data.decode())
            if self.message != None:
                self.tcp_server.send(self.message)
                self.message = None