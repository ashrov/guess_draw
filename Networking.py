import socket
import threading

default_host_adr = "127.0.0.1"

default_host_port = 6666

class Server:

    def __init__(self, host_adr=default_host_adr, host_port=default_host_port):
        self.clients = []
        self.server = socket.socket()
        self.server.bind((host_adr, host_port))
        self.server.listen(1)
        threading._start_new_thread(self.accept_clients, ())
        print("server started")


    def accept_clients(self):
        while True:
            conn, addr = self.server.accept()
            self.clients.append(conn)
            threading._start_new_thread(self.listen_client, (conn, addr))
            print("accepted another client")


    def listen_client(self, conn, addr):
        print(conn.recv(4096).decode('utf-8'))

        conn.send(f"welcome".encode("utf-8"))
        while True:
            message = conn.recv(4096).decode('utf-8')

            if not message:
                break

            print(f"got message {message}")

            self.send_to_all(message, (conn,))

        self.clients.remove(conn)



    def send_to_all(self, message, exceptions=()):
        for client in self.clients:
            if client in exceptions:
                continue
            else:
                client.send(f"{message}".encode("utf-8"))


class Client:

    def __init__(self, host_adr=default_host_adr, host_port=default_host_port):
        self.client = socket.socket()

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host_adr, host_port))
        self.send_message_to_server("Client Connected")

        self.window = None

        threading._start_new_thread(self.receive_message_from_server, ())


    def receive_message_from_server(self):
        while True:
            from_server = self.client.recv(4096).decode('utf-8')
            if not from_server:
                break

            self.parse_message(from_server)

        self.client.close()

    def set_window(self, window):
        self.window = window


    def parse_message(self, message):
        if len(message.split()) == 6:
            x1, y1, x2, y2, color, width = message.split()
            if self.window:
                self.window.draw_point_on_canvas(int(x1), int(y1), int(x2), int(y2), color, int(width))


    def send_message_to_server(self, message):
        self.client.send(message.encode("utf-8"))