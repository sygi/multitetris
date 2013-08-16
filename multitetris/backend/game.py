from .brick import Brick

import random

class Game(object):
    def __init__(self):
        """
        what is board? And what is bricks?
        """
        self.board = {}
        self.bricks = {}
        self.player_colors = {}
        self.player_pos = {}

        self.next_player_pos = 1

    def add_player(self, player_id):
        """
        Called when player connects.
        - player_id - opaque value
        """
        self.player_colors[player_id] = (
            random.randrange(100, 256),
            random.randrange(100, 256),
            random.randrange(100, 256))

        self.player_pos[player_id] = self.next_player_pos
        self.next_player_pos += 5
        self.next_player_pos %= self.get_board_size()[0]

    def get_board(self):
        '''
        Returns list of bricks.
        duck Brick:
        - pos - tuple of ints
        - color
        '''
        class BoardBrick:
            def __init__(self, pos, color):
                self.pos = pos
                self.color = color

        return self.bricks.values() + [
            BoardBrick(pos, color)
            for pos, color in self.board.items() ]

    def get_board_size(self):
        '''
        Returns board size
        '''
        return 40, 80

    def get_points(self):
        '''
        Returns dict of players' id and points
        '''
        return {'127.0.0.1': 300, 'localhost':150}

    def get_player_position(self, player_id):
        '''
        Returns player position
        '''
        return self.player_pos[player_id]

    def move(self, player_id, ch):
        """
        Called when client requests his brick to move.
        ch - passed from frontent
        player_id - opaque value to be stored in brick
        """
        print('MOVE %r' % ch)

    def tick(self):
        """Called each TICK_TIMEOUT."""
        for player_id, color in self.player_colors.items():
            if player_id not in self.bricks:
                brick = Brick(0,
                              (self.get_player_position(player_id),
                               self.get_board_size()[0],),
                              player_id, color)
                self.bricks[player_id] = brick

        for player_id, brick in self.bricks.items():
            brick.pos_y -= 1
            if brick.pos_y <= 0:
                del self.bricks[player_id]
