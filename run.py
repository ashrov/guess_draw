from PyQt5.QtWidgets import QApplication
from Canvas import Canvas, Paint
from Networking import Client, Server

import sys

def application():
    app = QApplication(sys.argv)

    try:
        client = Client()
    except ConnectionRefusedError:
        print("creating server, as no connection found")
        server = Server()
        client = Client()

    window = Paint(Canvas, client)

    window.show()


    sys._excepthook = sys.excepthook

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")


if __name__ == '__main__':
    application()


