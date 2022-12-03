import threading
import socket
from PyQt5.QtCore import QThread, pyqtSignal
import copy
import setting

FRAME_HEAD = [0x55,0x55,0x00]
CMD_MULT_SERVO_MOVE = 0x03
CMD_FULL_ACTION_RUN = 0x06
CMD_FULL_ACTION_STOP = 0x07
CMD_FULL_ACTION_ERASE = 0x08
CMD_ACTION_DOWNLOAD = 0x19


class NetWork(QThread):
    tcp_client_connected = pyqtSignal(tuple)
    def __init__(self):
        super(NetWork, self).__init__()
        self.message = None
        self.server_address = setting.net_address
        self.server_port = setting.net_port
        self.id_client = 0
        self.clients=[]
        self.tcp_server= []

    def set_address(self, address):
        self.server_address = address

    def set_port(self, port):
        self.server_port = port

    def tcp_server_setup(self):
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.tcp_server.bind((self.server_address, self.server_port))
        self.tcp_server.listen(128)

    def send(self,message):
        self.message = message

    def gesture_set(self,cnt,time,ids,pos):
        print("sent by net")
        print("parameter")
        print(cnt, time, ids, pos)
        temp = []
        length = 5
        time_high = time & 0xff00 >> 8  # 将时间拆分为高低八位
        time_low = time & 0xff
        for i in range(cnt):
            temp.append(ids[i])
            temp.append(pos[i] & 0xff)
            temp.append((pos[i] & 0xff00) >> 8)
            length += 3

        # 填装命令
        cmd = copy.deepcopy(FRAME_HEAD)
        cmd[2] = length
        cmd.append(CMD_MULT_SERVO_MOVE)
        cmd.append(cnt)
        cmd.append(time_low)
        cmd.append(time_high)
        cmd.extend(temp)
        # 串口发送命令
        self.send(cmd)

    def run(self):
        while True:
            client, client_address = self.tcp_server.accept()
            print("client connected")
            print(client_address)
            client = ClientThread(client,client_address[0],client_address[1])
            client.start()
            self.clients.append(client)
            self.tcp_client_connected.emit(client_address)
            if self.message != None:
                print(self.id_client)
                self.clients[self.id_client].load_message(self.message)


class ClientThread(QThread):
    def __init__(self,client,address,port):
        super(ClientThread, self).__init__()
        self.address = address
        self.port = port
        self.client = client
        self.message = None

    def load_message(self,message):
        self.message = message

    def gesture_set(self,cnt,time,ids,pos):
        print("sent by net")
        print("parameter")
        print(cnt, time, ids, pos)
        temp = []
        length = 5
        time_high = time & 0xff00 >> 8  # 将时间拆分为高低八位
        time_low = time & 0xff
        for i in range(cnt):
            temp.append(ids[i])
            temp.append(pos[i] & 0xff)
            temp.append((pos[i] & 0xff00) >> 8)
            length += 3

        # 填装命令
        cmd = copy.deepcopy(FRAME_HEAD)
        cmd[2] = length
        cmd.append(CMD_MULT_SERVO_MOVE)
        cmd.append(cnt)
        cmd.append(time_low)
        cmd.append(time_high)
        cmd.extend(temp)
        # 串口发送命令
        print(cmd)
        self.message = cmd

    def run(self):
        while True:
            # recv_data = self.client.recv(4096)
            # 6 有消息就回复数据，消息长度为0就是说明客户端下线了
            # if recv_data:
            #     print("客户端是:", self.address,self.port)
            #     print("客户端发来的消息是:", recv_data.decode())
            if self.message is not None:
                self.client.send(bytes(self.message))
                self.message = None