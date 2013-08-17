import unittest

#class TestBox(unittest.TestCase):
#	def test_create(self):
#		from multitetris.backend.brick import Box
#		box = Box(0,0,(1,2,3))

class TestBoard(unittest.TestCase):
	def test_create_board(self):
		from multitetris.backend.game import Game
		board = Game().get_board()

from multitetris.backend.brick import Brick, Type
class TestBrick(unittest.TestCase):
	def test_create_brick(self):
		brick = Brick(Type.STAIR, (1,1), 2, (1,2,3))

	def test_box_list(self):
		color = (3,2,1)
		pos = (2,2)
		brick = Brick(Type.LONG, pos, 3, color)
		box_list = brick.to_box_list()
		self.assertTrue(((pos[0], pos[1]+2), color) in box_list)

unittest.main()

