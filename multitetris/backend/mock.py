

class Game(object):
    def __init__(self):
        pass

    def get_state(self, addr):
        return {
            'clientId': addr,
            'msg': 'dupa',
            'bricks': [
                {"pos": [10, 20], "clientId": addr}
            ]
        }

    def write_move(self, ch):
        print 'MOVE %r' % ch

    def tick(self):
        print 'TICK!'
