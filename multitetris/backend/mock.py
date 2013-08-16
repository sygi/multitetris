

class Game(object):
    def __init__(self):
        pass

    def player_connected(self, ident):
        print 'PLAYER CONNECTED', ident

    def get_state(self, ident):
        return {
            'clientId': ident,
            'msg': 'dupa',
            'bricks': [
                {"pos": [10, 20], "clientId": ident}
            ]
        }

    def move(self, ch):
        print 'MOVE %r' % ch

    def tick(self):
        print 'TICK!'
