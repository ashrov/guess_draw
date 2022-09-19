import socket

from game import Game
from games_manager import GamesManager
import config


class Server:
    _games: list[Game]
    _games_manager = GamesManager()

    def __init__(self):
        self._sock = socket.socket()

    def start(self):
        self._sock.bind(config.SERVER_ADDR)

        while True:
            self.listen()

    def listen(self):
        self._sock.listen(1)
        conn, addr = self._sock.accept()
        self.handle(conn, addr)

    def handle(self, conn, addr):
        while msg := conn.recv(1024):
            msg.decode()
            conn.send(msg.upper())
            print(msg)

    def start_game(self, members):
        self._games.append(self._games_manager.create_new_game(members))


if __name__ == "__main__":
    server = Server()
    server.start()
