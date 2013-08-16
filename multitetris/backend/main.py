import threading
import socket
import json
import time

WRITE_TIMEOUT = 0.1
TICK_TIMEOUT = 0.1

global_lock = threading.Lock()

def main(game):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 9999))
    sock.listen(3)
    threading.Thread(target=ticker, args=[game]).start()
    while True:
        client_sock, addr = sock.accept()

        threading.Thread(target=client_reader, args=[game, addr, client_sock]).start()
        threading.Thread(target=client_writer, args=[game, addr, client_sock]).start()

def client_writer(game, addr, sock):
    while True:
        with global_lock:
            state = make_state(board=game.get_board(),
                               addr=addr)
        sock.sendall(json.dumps(state) + '\n')
        time.sleep(WRITE_TIMEOUT)

def make_state(board, addr):
    return {
        'client_id': addr,
        'bricks': [ {'pos': item.pos,
                     'player_id': item.player_id}
                    for item in board ]
    }

def client_reader(game, addr, sock):
    with global_lock:
        game.player_connected(addr)
    while True:
        move = sock.recv(1)
        if not move:
            break
        with global_lock:
            game.move(move)

def ticker(game):
    while True:
        with global_lock:
            game.tick()
        time.sleep(TICK_TIMEOUT)

if __name__ == '__main__':
    from .mock import Game
    main(Game())
