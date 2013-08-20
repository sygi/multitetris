from .brick import Brick

import random
import collections

class Game(object):

    def __init__(self):
        # Dictionary mapping position on the board to color
        # (contains only non-moving boxes)
        random.seed()
        self.board = {}
        # Dictionary mapping player_id to actually moving brick of that player
        self.bricks = {}

        self.width = 10
        self.height = 40
        self.width_per_player = 10 # It can be changed later

        self.players_numbers = {}
        #self.next_player_number = 0
        self.number_of_players = 0
        self.players_points = {}
        self.points_delta = 100 # It can be changed later, too

    def add_player(self, player_id):
        """
        Called when player connects.
        - player_id - opaque value
        """
        self.players_points[player_id] = 0
        self.players_numbers[player_id] = self.number_of_players
        self.number_of_players += 1
        self.width = self.number_of_players * self.width_per_player
        print "new player!", "number_of_players:", self.number_of_players, "board width:", self.width

    def _freeze_brick(self, brick):
        print 'freeze', brick.to_box_list(self.width)
        for box in brick.to_box_list(self.width):
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
        #No one knows what happens here
        #Returns dictionary mapping players' ids to their points
            NOPE, because returning self.players_points causes error in json.dumps(state)
        '''
        #return self.players_points;
        return {'127.0.0.1': 300, 'localhost': 150}

    def get_player_position(self, player_id):
        '''
        Returns position of player with given id
        '''
        #print "blabla %d" % (self.players_numbers[player_id]) * self.width_per_player
        return (self.players_numbers[player_id]) * self.width_per_player + self.width_per_player / 2 - 2
        #what the f* is going on here?
        # should work now

    def look_for_full_lines(self):
        '''
        Checks whether there are any full lines,
        removes them and returns number of such lines
        '''
        #(height, width) = self.get_board_size()
        #count_per_line = [0] * height
        #for box in self.board.keys():
        #    count_per_line[box[1]] += 1
        #    # ...
        # I think it should be reworked in the way as above

        removed_rows = 0
        (width, height) = self.get_board_size()
        for row in range(height):
            full_line = True
            # The method examines boxes on the board one by one
            for column in range(width):
                if (column, row) not in self.board:
                    full_line = False
                else:
                    # If any rows were removed, the box is moved down
                    color = self.board[(column, row)]
                    del self.board[(column, row)]
                    #self.board[(column, row - removed_rows)] = color
                    self.board[(column, row)] = color
            # If full line was found, all boxes it contains are removed
            if full_line == True:
                for column in range(width):
                    #del self.board[(column, row - removed_rows)]
                    del self.board[(column, row)]
                removed_rows += 1
                # full palowanie-fix
                board1 = {}
                for row1 in range(row):
                    for col1 in range(width):
                        if (col1, row1) in self.board:
                            color1 = self.board[(col1, row1)]
                            del self.board[(col1, row1)]
                            board1[(col1, row1+1)] = color1
                for boxkey in board1.keys():
                    self.board[boxkey] = board1[boxkey]
        #print "BOARD", self.board
        return removed_rows

    def move(self, player_id, ch):
        """
        Called when client requests his brick to move.
        Returns True if the brick was moved successfully, False otherwise.
        ch - passed from frontent ("L","R","U","D")
        player_id - opaque value to be stored in brick
        """
        if player_id not in self.bricks.keys():
            # if there was no active brick and the player moved (or we just received his packet),
            # the thread would crash
            return False
        player_brick = self.bricks[player_id]
        functions = {
            'U': (player_brick.rotate, player_brick.rotate_back),
            'L': (player_brick.move_left, player_brick.move_right),
            'R': (player_brick.move_right, player_brick.move_left),
            'D': (player_brick.move_down, player_brick.move_up),
            }
        if ch in functions:
            do, do_back = functions[ch]
            do(self.width)
            if player_brick.is_collision_with_board(
                    self.bricks, self.board, self.width, self.height):
                do_back(self.width)
            else:
                return True
        return False

    def tick(self):
        """Called each TICK_TIMEOUT."""
        for player_id in self.players_points.keys():
            color = (random.randrange(256), random.randrange(256), random.randrange(256)) # needs to be changed
            if player_id not in self.bricks:
                brick = Brick(random.randint(0,4),
                              (self.get_player_position(player_id),
                               0),
                              player_id, color)
                self.bricks[player_id] = brick
        for player_id, brick in self.bricks.items():
            #print 'brick.pos', brick.pos
            if not self.move(player_id, 'D'):
                self._freeze_brick(brick)
                del self.bricks[player_id]
                new_full_lines_number = self.look_for_full_lines();
                #print "!!! FULL_LINE !!!", new_full_lines_number
                self.players_points[player_id] += self.points_delta * new_full_lines_number
                print 'players_points: ', self.players_points
