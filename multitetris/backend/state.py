
class Brick(object):    
    """
    One 4-box brick in move
    """
    class Type(object):
        LONG, DUCK_L, DUCK_R, SQR, STAIR = range(5)
        
    def __init__(self, board, enum, pos_x, pos_y, player_id, color):
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
        self.state = 0
        self.color = color
        self.player_id = player_id
        self.board = board
        
    def to_box_list():
        #box_look = self.state_table[self.state]
        ls = []
        for iy in range(4):
            for ix in range(4):
                if self.state_table[self.state][iy][ix] == "1":
                    ls.append(Box(self.pos_x + ix, self.pos_y + 3 - iy, self.color))
        return ls    
    """    
    def is_collision_with_brick(brick):
        enemy_boxes = brick.to_box_list()
        for my_box in self.to_box_list():
            for enemy_box in enemy_boxes:
                if enemy_box.x == my_box.x and enemy_box.y == my_box.y:
                    return True
    """
    
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
            
    pass

class Box(object):
    """
    Represents one box in board
    """
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
