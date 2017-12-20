from utils import utils
from utils.euclidean import Point, Grid
from utils.euclidean import NORTH, SOUTH, EAST, WEST, Vector
from itertools import dropwhile, accumulate, repeat, chain


def find_perpendicular_direction(grid: Grid, position: Point, cur_direction: Vector):
    if cur_direction in [NORTH, SOUTH]:
        directions = [EAST, WEST]
    else:
        directions = [NORTH, SOUTH]
    for direction in directions:
        if grid.get(position + direction, ' ') != ' ':
            return direction


def follow_path(grid: Grid):
    start = Point(0, 0)
    # Keep moving east until we find a point not equal to ' '
    point = next(
             dropwhile(
                 lambda x: grid[x] == ' ',
                 accumulate(chain.from_iterable(([start], repeat(EAST))))))
    cur_direction = SOUTH if grid[point] == '|' else EAST
    yield grid[point]
    observed_letters = []
    while True:
        # look in the direction we're heading
        ahead = point + cur_direction
        grid_ahead = grid.get(ahead, ' ')
        if grid_ahead != ' ':
            if grid_ahead.isalnum():
                observed_letters.append(grid_ahead)
            elif grid_ahead == '+':
                cur_direction = find_perpendicular_direction(
                    grid, ahead, cur_direction
                )
            point = ahead
            yield grid_ahead
        else:
            break


def main():
    rows = [line.strip('\n') for line in utils.get_data(19)]
    grid = Grid([[i for i in row] for row in rows])
    steps = list(follow_path(grid))
    print('Part 1: ' + ''.join([x for x in steps if x.isalnum()]))
    print(f'Part 2: {len(steps)}')


if __name__ == '__main__':
    main()
