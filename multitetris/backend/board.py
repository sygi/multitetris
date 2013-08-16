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
	
	
	def brick_at_pos(self, x, y):
		"""
		Returns the block at position [x, y] or None if the position is empty
		"""
		return __brick_arr[x % __width][y % __height]
	
	
	def broaden(self, new_width):
		if (new_width < __width)
			raise Exception("Board shrinking is not yet unimplemented!")
		
		'''Append empty fields'''
		__brick_arr.extend([[None]*__height for _ in xrange(new_width - __width)])
		__width = new_width
	
	
	def get_size(self)
		"""
		Gets board's size as [w, h]
		"""
		return [__width, __height]
	
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
	

