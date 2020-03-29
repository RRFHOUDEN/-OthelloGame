import socket
import datetime
import sys
class Server():
    def __init__(self):
        self.PORT = 50000
        self.BUFSIZE = 4096

    def setting(self):
        #make_socket
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #setting_addrres
        server.bind(("", self.PORT))
        #waiting_listen
        server.listen()

        self.client, self.addr = server.accept()  # 通信用ソケットの取得
        print("setting done")

    def get(self):
        return self.client.recv(self.BUFSIZE).decode("utf-8")

    def send(self, msg):
        self.client.sendall(msg.encode("utf-8"))

    def close_connection(self):
        self.client.close()                             # コネクションのクローズ

class Client():
    def __init__(self):
        self.PORT = 50000  # ポート番号
        self.BUFSIZE = 4096  # 受信バッファの大きさ

    def setting(self, host):
        #make_client
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #connect_server
        print(host)
        try:
            self.client.connect((host, self.PORT))
        except:
            print("Can't connect")
            sys.exit()

    def send(self, msg):
        self.client.sendall(msg.encode("utf-8"))

    def get(self):
        return self.client.recv(self.BUFSIZE).decode("utf-8")

    def close_connection(self):
        self.client.close()

def server_func():
    server = Server()
    server.setting()
    print(server.get())
    server.send("hello world")
    server.close_connection()

def client_func():
    client = Client()
    client.setting("localhost")
    client.send("helloServer")
    print(client.get())
    client.close_connection()

mode = int(input())
if mode == 1:
    server_func()
else:
    client_func()