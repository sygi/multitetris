from pygame import Color

"""
Usage:

from common import consts
-or-
from common import consts as frontend_consts

and so on.
"""

class consts:
    pass

consts.__dict__ = {
    'block_element_size': 5,
    'number_of_rows': 30,
    'columns_per_player': 10,
    'max_players': 10,
    'window_width': 800,
    'window_height': 600,
    'tab_width': 200}

colors = {
    'semirandom': Color(123, 230, 58),
    'block_inner': Color(192, 73, 239),
    'block_border': Color(23, 45, 32),
}
