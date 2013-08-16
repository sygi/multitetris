import threading
import socket
import json

class Connection(object):
    def __init__(self, ip_address, on_update):
        self.ip_address = ip_address
        self.on_update = on_update
        # TODO: connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip_address, 9999))
        # TODO: thread
        
    
    def _run(self):
        pass
    
    def move(self, move):
        pass
    
    def disconnect(self):
        pass
    
if __name__ == "__main__":
    Connection("127.0.0.1", None)
