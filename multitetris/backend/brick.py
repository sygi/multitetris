class Type(object):
    LONG, DUCK_L, DUCK_R, SQR, STAIR = range(5)

class Brick(object):
    """
    One 4-box brick in move
    """
    def __init__(self, enum, pos, player_id, color):
        self.pos_x, self.pos_y = pos
        self.init_type(enum, self.pos_x, self.pos_y)
        self.state = 0
        self.color = color
        self.player_id = player_id

    @property
    def pos(self):
        return self.pos_x, self.pos_y

    def init_type(self, enum, pos_x, pos_y):
        if enum == Type.LONG:
            self.state_table = [
                ["0100","0100","0100","0100"],
                ["0000","0000","0000","1111"],
                ["0100","0100","0100","0100"],
                ["0000","0000","0000","1111"]]
            self.pos_x = pos_x+3
            self.pos_y = pos_y-1
        elif enum == Type.DUCK_L:
            self.state_table = [
                ["0000","0000","0110","1100"],
                ["0000","1000","1100","0100"],
                ["0000","0000","0110","1100"],
                ["0000","1000","1100","0100"]]
            self.pos_x = pos_x+1
            self.pos_y = pos_y-1
        elif enum == Type.DUCK_R:
            self.state_table = [
                ["0000","0000","1100","0110"],
                ["0000","0100","1100","1000"],
                ["0000","0000","1100","0110"],
                ["0000","0100","1100","1000"]]
            self.pos_x = pos_x+1
            self.pos_y = pos_y-1
        elif enum == Type.SQR:
            self.state_table = [
                ["0000","0000","1100","1100"],
                ["0000","0000","1100","1100"],
                ["0000","0000","1100","1100"],
                ["0000","0000","1100","1100"]]
            self.pos_x = pos_x+1
            self.pos_y = pos_y-1
        elif enum == Type.STAIR:
            self.state_table = [
                ["0000","0000","0100","1110"],
                ["0000","0100","1100","0100"],
                ["0000","0000","1110","0100"],
                ["0000","1000","1100","1000"]]
            self.pos_x = pos_x+1
            self.pos_y = pos_y-1

    def to_box_list(self):
        ls = []
        for iy in range(4):
            for ix in range(4):
                if self.state_table[self.state][iy][ix] == "1":
                    ls.append((self.pos_x + ix, self.pos_y + 3 - iy))
        return ls

    # we're looking for collisions with board other than with
    # the brick former self
    def is_collision_with_board(old_box_list):
        new_box_list = self.to_box_list()
        for i in len(new_box_list):
            for old_box in old_box_list:
                if new_box_list[i].x == old_box.x and new_box_list[i].y == old_box.y:
                    del new_box_list[i]
        for box in new_box_list:
            if self.board.is_box_at(box.x,box.y):
                return True

                """
    def collides_with_board(self, board):
        for box in self.to_box_list():
            if (box.x, box.y) in board:
                return True

        return False

    def is_collision_with_brick(brick):
        enemy_boxes = brick.to_box_list()
        for my_box in self.to_box_list():
            for enemy_box in enemy_boxes:
                if enemy_box.x == my_box.x and enemy_box.y == my_box.y:
                    return True
"""

class Box(object):
    """
    Represents one box in board
    """
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
    	return "(%d, %d, color)" % (self.x, self.y)
