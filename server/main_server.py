import socket

from game import Game
from games_manager import GamesManager

import config

import asyncio


class Server:
    _games: list[Game]
    _games_manager = GamesManager()
    _sock = socket.socket()

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
            conn.send(msg.upper())
            print(msg.decode())

    def start_game(self, members):
        self._games.append(self._games_manager.create_new_game(members))

    def __aexit__(self, *exc):
        pass
