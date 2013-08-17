import threading
import socket
import json
import Queue
import sys

class Connection(object):
    def __init__(self, ip_address, on_update):
        self.ip_address = ip_address
        self.on_update = on_update
        self.state = None
        # connection
        self.sock = socket.socket()
        self.sock.connect((ip_address, 9999))
        self.sockf = self.sock.makefile('w+')
        # thread
        threading.Thread(target=self._run).start()

    def _run(self):
        while True:
            line = self.sockf.readline()
            if not line:
                print 'Server died.'
                sys.exit()
            self.state = json.loads(line)

    def move(self, move):
        threading.Thread(target=
                         lambda: self.sock.sendall(move)).start()

    def disconnect(self):
        print 'not disconnecting'

if __name__ == "__main__":
    Connection("127.0.0.1", None)
