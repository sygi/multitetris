import unittest

class TestBox(unittest.TestCase):
	def test_create(self):
		from multitetris.backend.state import Box
		box = Box(0,0,(1,2,3))

class TestBoard(unittest.TestCase):
	def test_create_board(self):
		from multitetris.backend.game import Game
		board = Game().get_board()

unittest.main()

