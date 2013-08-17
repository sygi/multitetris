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
                ["0100","0100","0100","0100"],
                ["0000","0000","0000","1111"],
                ["0100","0100","0100","0100"],
                ["0000","0000","0000","1111"]]
            self.pos_y = pos_y+3
            self.pos_x = pos_x-1
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

    #boxes are touples: BoardBrick((pos_x,pos_y),color)
    def to_box_list(self):
        ls = []
        for iy in range(4):
            for ix in range(4):
                if self.state_table[self.state][iy][ix] == "1":
                    ls.append(BoardBrick(
                        (self.pos_x + ix, self.pos_y - iy),
                        self.color))
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
                
    def rotate(self):
        self.self_state += 1
        self.self_state %= 4
    
    def rotate_back(self):
        self.self_state += 3
        self.self_state %= 4
        
    def move_left(self):
        self.pos_x -= 1
        
    def move_right(self):
        self.pos_x += 1
        
    def move_down(self):
        self.pos_y += 1
        
    def move_up(self):
        self.pos_y -= 1
        

BoardBrick = collections.namedtuple('BoardBrick', 'pos color')
