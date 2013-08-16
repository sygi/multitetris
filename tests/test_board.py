import unittest

class TestBox(unittest.TestCase):
	def test_create(self):
		from multitetris.backend.state import Box
		box = Box(0,0,(1,2,3))

class TestBoard(unittest.TestCase):
	def test_create_board(self):
		from multitetris.backend.game import Game
		board = Game().get_board()

from multitetris.backend.state import Brick, Type
class TestBrick(unittest.TestCase):
	def test_create_brick(self):
		brick = Brick(Type.LONG, (1,1), 2, (1,2,3))

	def test_create_brick(self):
		brick = Brick(Type.STAIR, (2,2), 3, (3,2,1))
		self.assertTrue(len(brick.to_box_list()) == 4)

unittest.main()

