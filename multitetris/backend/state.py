
class Game(object):
    """
    Has board and game state (players info, etc)
    """
    
    def __init__(self):
        pass

    def player_connected(self, player_id):
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
        

class Board(object):
    """
    Whole board, has bricks and boxes
    """
    pass

class Brick(object):	
    """
    One 4-box brick in move
    """
	class Type(object):
		LONG, DUCK, SQR, STAIR = range(4)
	def __init__(self, enum, pos_x, pos_y):
		if (enum == Type.LONG):
			self.state_table = [
			["0100","0100","0100","0100"],
			["0000","0000","0000","1111"],
			["0100","0100","0100","0100"],
			["0000","0000","0000","1111"]]
		elif (enum == Type.DUCK):
			self.state_table = [
			["0000","0000","0110","1100"],
			["0000","1000","1100","0100"],
			["0000","0000","0110","1100"],
			["0000","1000","1100","0100"]]
		elif (enum == Type.SQR):
			self.state_table = [
			["0000","0000","1100","1100"],
			["0000","0000","1100","1100"],
			["0000","0000","1100","1100"],
			["0000","0000","1100","1100"]]
		elif (enum == Type.STAIR):
			self.state_table = [
			["0000","0000","0100","1110"],
			["0000","0100","1100","0100"],
			["0000","0000","1110","0100"],
			["0000","1000","1100","1000"]]
		self.state = 0;
			
    pass

class Box(object):
    """
    Represents one box in board
    """
    pass
