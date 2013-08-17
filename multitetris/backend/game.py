from .brick import Brick

import random
import collections


class Game(object):

    def __init__(self):
        # Dictionary mapping position on the board to color
        # (contains only non-moving boxes)
        self.board = {}
        # Dictionary mapping player_id to actually moving brick of that player
        self.bricks = {}

        self.width = 10
        self.height = 100

        self.height = 40
        self.width_per_player = 10 # It can be changed later

        self.players_numbers = {}
        self.next_player_number = 0
        self.players_points = {}
        self.points_delta = 100 # It can be changed later, too

    def add_player(self, player_id):
        """
        Called when player connects.
        - player_id - opaque value
        """
        self.players_points[player_id] = 0
        self.players_numbers[player_id] = self.next_player_number
        self.next_player_number += 1
        self.width = players_points.len() * width_per_player

    def _freeze_brick(self, brick):
        print 'freeze', brick.to_box_list()
        for box in brick.to_box_list():
            self.board[box.pos] = box.color

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
            board += brick.to_box_list(self.width)
        return board

    def get_board_size(self):
        '''
        Returns board size
        '''
        return self.width, self.height

    def get_points(self):
        '''
        No one knows what happens here
        '''
        return {'127.0.0.1': 300, 'localhost': 150}

    def get_player_position(self, player_id):
        '''
        Returns position of player with given id
        '''
        return (self.players_numbers[player_id] - 1) * self.width_per_player

    def look_for_full_lines(self):
        '''
        Checks whether there are any full lines,
        removes them and returns number of such lines
        '''
        removed_rows = 0
        (height, width) = self.get_board_size()
        for row in range(0, height-1):
            full_line = True
            # The method examines boxes on the board one by one
            for column in range(0, width-1):
                if (column, row) not in board:
                    full_line = False
                else:
                    # If any rows were removed, the box is moved down
                    color = board[(column, row)]
                    del board[(column, row)]
                    board[(column, row - removed_rows)] = color
            # If full line was found, all boxes it contains are removed
            if full_line == True:
                for column in range(0, width-1):
                    del board[(column - remowed_rows, row)]
                removed_rows += 1
        return removed_rows

    def move(self, player_id, ch):
        """
        Called when client requests his brick to move.
        Returns True if the brick was moved successfully, False otherwise.
        ch - passed from frontent ("L","R","U","D")
        player_id - opaque value to be stored in brick
        """
        player_brick = self.bricks[player_id]
        functions = {
            'U': (player_brick.rotate, player_brick.rotate_back),
            'L': (player_brick.move_left, player_brick.move_right),
            'R': (player_brick.move_right, player_brick.move_left),
            'D': (player_brick.move_up, player_brick.move_down),
            }
        if ch in functions:
            do, do_back = functions[ch]
            do(self.width)
            if player_brick.is_collision_with_board(
                    self.board, self.bricks, self.width, self.height):
                do_back(self.width)
            else:
                return True
        return False

    def tick(self):
        """Called each TICK_TIMEOUT."""
        for player_id in self.players_points.keys():
            color = (128, 0, 128)
            if player_id not in self.bricks:
                brick = Brick(0,
                              (self.get_player_position(player_id),
                               0),
                              player_id, color)
                self.bricks[player_id] = brick
        for player_id, brick in self.bricks.items():
            if not self.move(player_id, 'D'):
                self._freeze_brick(brick)
