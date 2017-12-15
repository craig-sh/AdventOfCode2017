from utils import utils
from day_10 import get_knot_hash
from utils.euclidean import Point
from utils.euclidean import COUNTER_CLOCKWISE
from collections import defaultdict


GRID_SIZE = 128
data = list(utils.get_data(14))[0].strip()

ones = set()
marks = {}
group_num = 0

for row in range(GRID_SIZE):
    knot = get_knot_hash(f'{data}-{row}')
    bits = ''.join([bin(int(char, 16))[2:].zfill(4) for char in knot])
    ones.update(((Point(col, row) for col, bit in enumerate(bits) if bit == '1')))


def mark(point: Point, cur_group=None):
    if point in marks or point not in ones:
        return
    if cur_group is None:
        global group_num
        group_num += 1
    marks[point] = group_num
    for direction in COUNTER_CLOCKWISE:
        mark(point + direction, group_num)


for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        mark(Point(col, row))


print(f'Part 1: {len(ones)}')
print(f'Part 2: {group_num}')
