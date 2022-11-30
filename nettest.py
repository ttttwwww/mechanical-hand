import socket
import setting
import threading

address = setting.net_address
port = setting.net_port


def dispose_client_request(tcp_client_1, tcp_client_address):
    # 5 循环接收和发送数据
    while True:
        recv_data = tcp_client_1.recv(4096)

        # 6 有消息就回复数据，消息长度为0就是说明客户端下线了
        if recv_data:
            print("客户端是:", tcp_client_address)
            print("客户端发来的消息是:", recv_data.decode())
            send_data = "message_received\r\n".encode()
            tcp_client_1.send(send_data)
        else:
            print("%s 客户端下线了..." % tcp_client_address[1])
            tcp_client_1.close()
            break


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server.bind((address,port))
    server.listen(128)
    client, client_address= server.accept()
    print("客户端的ip地址和端口号:", client_address)
    dispose_client_request(client,client_address)