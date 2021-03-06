import collections


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
                ["0100", "0100", "0100", "0100"],
                ["0000", "0000", "0000", "1111"],
                ["0100", "0100", "0100", "0100"],
                ["0000", "0000", "0000", "1111"]]
            self.pos_y = pos_y + 3
            self.pos_x = pos_x - 1
        elif enum == Type.DUCK_L:
            self.state_table = [
                ["0000", "0000", "0110", "1100"],
                ["0000", "1000", "1100", "0100"],
                ["0000", "0000", "0110", "1100"],
                ["0000", "1000", "1100", "0100"]]
            self.pos_x = pos_x + 1
            self.pos_y = pos_y - 1
        elif enum == Type.DUCK_R:
            self.state_table = [
                ["0000", "0000", "1100", "0110"],
                ["0000", "0100", "1100", "1000"],
                ["0000", "0000", "1100", "0110"],
                ["0000", "0100", "1100", "1000"]]
            self.pos_x = pos_x + 1
            self.pos_y = pos_y - 1
        elif enum == Type.SQR:
            self.state_table = [
                ["0000", "0000", "1100", "1100"],
                ["0000", "0000", "1100", "1100"],
                ["0000", "0000", "1100", "1100"],
                ["0000", "0000", "1100", "1100"]]
            self.pos_x = pos_x + 1
            self.pos_y = pos_y - 1
        elif enum == Type.STAIR:
            self.state_table = [
                ["0000", "0000", "0100", "1110"],
                ["0000", "0100", "1100", "0100"],
                ["0000", "0000", "1110", "0100"],
                ["0000", "1000", "1100", "1000"]]
            self.pos_x = pos_x + 1
            self.pos_y = pos_y - 1

    # boxes are touples: BoardBrick((pos_x,pos_y),color)
    def to_box_list(self, board_width):
        """
        Returns list of BoardBricks (boxes);
        """
        ls = []
        for iy in range(4):
            for ix in range(4):
                if self.state_table[self.state][iy][ix] == "1":
                    ls.append(BoardBrick(
                        ((self.pos_x + ix) % board_width, self.pos_y - iy),
                        self.color))
        return ls

    # we're looking for collisions with board other than with
    # the brick former self

    def rotate(self, board_width):
        self.state += 1
        self.state %= 4

    def rotate_back(self, board_width):
        self.state += 3
        self.state %= 4

    def move_left(self, board_width):
        self.pos_x -= 1
        self.pos_x %= board_width

    def move_right(self, board_width):
        self.pos_x += 1
        self.pos_x %= board_width

    def move_down(self, board_width):
        self.pos_y += 1

    def move_up(self, board_width):
        self.pos_y -= 1

    def is_collision_with_board(self, bricks, board, board_width, board_height):
        """
        returns True on collision
        """
        self_boxes = self.to_box_list(board_width)
        for box in self_boxes:
            if box.pos[1] >= board_height:
                print 'stopping of height', self.pos
                return True

        for brick in bricks.values():
            if brick is self:
                continue
            for box in brick.to_box_list(board_width):
                for self_box in self_boxes:
                    if self_box.pos == box.pos:
                        return True

        for box_pos in board.keys():
            for self_box in self_boxes:
                if self_box.pos == box_pos:
                    return True
        return False

BoardBrick = collections.namedtuple('BoardBrick', 'pos color')
