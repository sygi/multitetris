from .board import Board

class Game(object):
    def __init__(self):
        Board board();
        self.board = Board()
        self.players = {}
        self.next_player_id = 1

    def player_connected(self, player_id):
        """
        Called when player connects.
        - player_id - opaque value
        """
        print('PLAYER CONNECTED', player_id)

    def get_board(self):
        """
        Returns list of bricks.
        duck Brick:
        - pos - tuple of ints
        - player_id - opaque value passed by move/player_connected
        """
        class FakeBrick:
            pos = [10, 10]
            player_id = ('localhost', 12)
        return [FakeBrick()]

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
