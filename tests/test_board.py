import unittest

class TestBoard(unittest.TestCase):
	def test_create_board(self):
		from multitetris.backend.game import Game
		board = Game().get_board()

from multitetris.backend.brick import Brick, Type, BoardBrick
class TestBrick(unittest.TestCase):
	def test_create_brick(self):
		brick = Brick(Type.STAIR, (1,1), 2, (1,2,3))

	def test_box_list(self):
		color = (3,2,1)
		pos = (2,2)
		brick = Brick(Type.LONG, pos, 3, color)
		box_list = brick.to_box_list()
		self.assertTrue(BoardBrick((pos[0], pos[1]+2), color) in box_list)

	def test_brick_rotate(self):
		color = (3,2,1)
		pos = (3,1)
		brick = Brick(Type.LONG, pos, 2, color)
		brick.rotate()
		box_list = brick.to_box_list()
		self.assertTrue(BoardBrick(pos=(5,4), color=color) in box_list)

from multitetris.backend.game import Game

class TestGame(unittest.TestCase):
	def test_game_init(self):
		game = Game()
	def test_move_brick(self):
		game = Game()
		one_brick = Brick(Type.STAIR, (0, 2), 1, (1, 3, 2))
		# starts with (1, 1)
		game.bricks[1] = one_brick
		game.move(1, 'R')
		self.assertTrue(one_brick.pos_x == 2)
		game.move(1, 'L')
		self.assertTrue(one_brick.pos_x == 1)

unittest.main()

