

class Game(object):
    def __init__(self):
        pass

    def add_player(self, player_id):
        '''
        Called when player connects.
        - player_id - opaque value
        '''
        print 'PLAYER CONNECTED', player_id

    def get_board(self):
        '''
        Returns list of bricks.
        duck Brick:
        - pos - tuple of ints
        - player_id - opaque value passed by move/player_connected
        '''
        class FakeBrick:
            pos = [10, 10]
            player_id = ('localhost', 12)
        return [FakeBrick()]
    
    def get_points(self):
        '''
        Returns list of players' points
        '''
        print 'POINTS GOT'
    
    def start(self):
        '''
        Called when game starts, before any ticks.
        '''
        print 'START'
    
    def move(self, player_id, ch):
        '''
        Called when client requests his brick to move.
        ch - passed from frontent
        player_id - opaque value to be stored in brick
        '''
        print 'MOVE %r' % ch

    def tick(self):
        '''
        Called each TICK_TIMEOUT.
        '''
        print 'TICK!'
