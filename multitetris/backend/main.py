import threading
import socket

def main():
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 9999))
    sock.listen(3)
    while True:
        client_sock, addr = sock.accept()

        threading.Thread(target=client_run, args=[addr, client_sock]).start()

def client_run(addr, sock):
    print addr, sock

if __name__ == '__main__':
    main()
