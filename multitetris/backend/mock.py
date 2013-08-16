class Game(object):
    def __init__(self):
        pass

    def add_player(self, player_id):
        '''
        Called when player connects.
        - player_id - opaque value
        '''
        print('PLAYER CONNECTED', player_id)

    def get_board(self):
        '''
        Returns list of bricks.
        duck Brick:
        - pos - tuple of ints
        - player_id - opaque value passed by move/player_connected
        '''
        class FakeBrick:
            pos = (10, 10)
            color = (15, 124, 67)
        return [FakeBrick()]
    
    def get_board_size(self):
        '''
        Returns board size
        '''
        return 80, 25
    
    def get_points(self):
        '''
        Returns dict of players' id and points
        '''
        return {'127.0.0.1': 300, 'localhost':150}
    
    def start(self):
        '''
        Called when game starts, before any ticks.
        '''
        print 'START'
    
    def get_player_position(player_id):
        '''
        Returns player position
        '''
        return 15
    
    def move(self, player_id, ch):
        """
        Called when client requests his brick to move.
        ch - passed from frontent
        player_id - opaque value to be stored in brick
        """
        print('MOVE %r' % ch)

    def tick(self):
        """
        Called each TICK_TIMEOUT.
        """
        print('TICK!')
