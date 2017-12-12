from utils import utils
from utils.hex_points import HexPoint
from utils.hex_points import NORTH, SOUTH, NORTH_EAST,\
    NORTH_WEST, SOUTH_EAST, SOUTH_WEST


DMAP = {
    'n': NORTH,
    's': SOUTH,
    'ne': NORTH_EAST,
    'nw': NORTH_WEST,
    'se': SOUTH_EAST,
    'sw': SOUTH_WEST,
}

steps = utils.get_single_line_split(11, ',')
origin = HexPoint(0, 0, 0)
location = HexPoint(0, 0, 0)
max_dist = cur_dist = 0
final_distance: int
for step in steps:
    location += DMAP[step]
    cur_dist = location.distance(origin)
    max_dist = max(max_dist, cur_dist)

print(f'Part 1: {cur_dist}')
print(f'Part 2: {max_dist}')
