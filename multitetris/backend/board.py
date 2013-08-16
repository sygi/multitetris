from .mock import Box

class Board(object):
	"""
	This class contains the board state.
	"""
	
	def __init__(self, width, height):
		"""
		Constructor...
		"""
		self.__width = width
		self.__height = height
		self.__brick_arr = [[None]*__height for _ in xrange(__width)]
	
	
	def is_brick_at_pos(self, x, y):
		"""
		Returns True if there is a block at (x, y);
		"""
		x %= __width
		y %= __height
		return __brick_arr[x][y] is None
	
	
	def broaden(self, new_width):
		if (new_width < __width)
			raise Exception("Board shrinking is not yet unimplemented!")
		
		'''Append empty fields'''
		__brick_arr.extend([[None]*__height for _ in xrange(new_width - __width)])
		__width = new_width
	
	
	def get_width(self):
		"""
		Returns width.
		"""
		return __width
	
	
	def get_height(self):
		"""
		Return height.
		"""
		return ___height
	
	
	def get_state(self):
		"""
		Gets the state of the board.
		"""
		return __brick_arr
	
	
	def assimilate(self, boxes):
		"""
		Writes boxes into the board
		"""
		for box in boxes:
			
		
		pass
	

