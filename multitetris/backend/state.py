
class Brick(object):	
    """
    One 4-box brick in move
    """
	class Type(object):
		LONG, DUCK, SQR, STAIR = range(4)
	def __init__(self, enum, pos_x, pos_y, player_id, color):
		if (enum == Type.LONG):
			self.state_table = [
			["0100","0100","0100","0100"],
			["0000","0000","0000","1111"],
			["0100","0100","0100","0100"],
			["0000","0000","0000","1111"]]
			self.pos_x = pos_x+3
			self.pos_y = pos_y-1
		elif (enum == Type.DUCK):
			self.state_table = [
			["0000","0000","0110","1100"],
			["0000","1000","1100","0100"],
			["0000","0000","0110","1100"],
			["0000","1000","1100","0100"]]
			self.pos_x = pos_x+1
			self.pos_y = pos_y-1
		elif (enum == Type.SQR):
			self.state_table = [
			["0000","0000","1100","1100"],
			["0000","0000","1100","1100"],
			["0000","0000","1100","1100"],
			["0000","0000","1100","1100"]]
			self.pos_x = pos_x+1
			self.pos_y = pos_y-1
		elif (enum == Type.STAIR):
			self.state_table = [
			["0000","0000","0100","1110"],
			["0000","0100","1100","0100"],
			["0000","0000","1110","0100"],
			["0000","1000","1100","1000"]]
			self.pos_x = pos_x+1
			self.pos_y = pos_y-1
		self.state = 0
		self.color = color
		self.player_id = player_id
		
	def to_box_list():
		#box_look = self.state_table[self.state]
		ls = []
		for(iy in range(4)):
			for(ix in range(4)):
				if(self.state_table[self.state][iy][ix] == "1"):
					ls.append(Box(self.pos_x - 4 + ix
			
			
			
    pass

class Box(object):
    """
    Represents one box in board
    """
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
