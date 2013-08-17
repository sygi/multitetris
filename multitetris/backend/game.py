from .brick import Brick

import random
import collections


class Game(object):

    def __init__(self):
        """
        Dictionary mapping position on the board to color
        (contains only non-moving boxes)
        """
        self.board = {}
        """
        Dictionary mapping player_id to actually moving brick of that player
        """
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
        Returns list of BoardBricks.
        duck Brick:
        - pos - tuple of ints
        - color
        '''
        BoardBrick = collections.namedtuple('BoardBrick', 'pos color')
        board = [
            BoardBrick(pos, color)
            for pos, color in self.board.items()]
        for brick in self.bricks.values():
            board += brick.to_box_list()
        return board

    def get_board_size(self):
        '''
        Returns board size
        '''
        return 40, 80

    def get_points(self):
        '''(2, 4, color)
        Returns dict of players' id and points
        '''
        return {'127.0.0.1': 300, 'localhost': 150}

    def get_player_position(self, player_id):
        '''
        Returns player position
        '''
        return self.player_pos[player_id]

    def move(self, player_id, ch):
        """
        Called when client requests his brick to move.
        Returns True if the brick was moved successfully, False otherwise.
        ch - passed from frontent ("L","R","U","D")
        player_id - opaque value to be stored in brick
        """
        player_brick = self.bricks[player.id]
        
        if ch == 'U':
            player_brick.rotate()
            if player_brick.is_collision_with_board(self.board):
                player_brick.rotate_back();
                return False
        
        else if ch == 'L'
            player_brick.move_left()
            if player_brick.is_collision_with_board(self.board)
                player_brick.move_right()
                return False
        
        else if ch == 'R'
            player_brick.move_right()
            if player_brick.is_collision_with_board(self.board)
                player_brick.move_left()
                return False
        
        else if ch == 'D'
            player_brick.move_down()
            if player_brick.is_collision_with_board(self.board)
                player_brick.move_up()
                return False
        
        return True

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
            if brick.pos_y <= 3: # TODO
                del self.bricks[player_id]
                self._freeze_brick(brick)

    def _freeze_brick(self, brick):
        print 'freeze', brick.to_box_list()
        for box in brick.to_box_list():
            self.board[box.pos] = box.color
