from itertools import cycle, islice
from typing import Generator
from utils import utils
from utils.euclidean import COUNTER_CLOCKWISE, DIAG, Point


def move_spirally() -> Generator[Point, None, None]:
    """ Spiral infinitely outwards from the origin.
    After each step yield the current location
    """
    position = Point(0, 0)
    distance = 0
    for i, direction in enumerate(cycle(COUNTER_CLOCKWISE)):
        if i % 2 == 0:
            distance += 1
        for _ in range(distance):
            yield position
            position += direction


def find_manhattan_distance(num: int) -> int:
    num_position = next(islice(move_spirally(), num - 1, num))
    return abs(num_position.x) + abs(num_position.y)


def find_adjacent_sum(threshold: int) -> int:
    values = {Point(0, 0): 1}
    for position in move_spirally():
        if position == Point(0, 0):
            continue
        adjacent_sum = sum(values.get(position + x, 0)
                           for x in DIAG)
        if adjacent_sum > threshold:
            return adjacent_sum
        values[position] = adjacent_sum


if __name__ == '__main__':
    for data, answer in [(1, 0), (12, 3), (23, 2), (1024, 31)]:
        assert find_manhattan_distance(data) == answer

    data = int(list(utils.get_data(3))[0].strip())
    distance = find_manhattan_distance(data)
    print(f'Part 1: {distance}')

    for data, answer in [(3, 4), (746, 747)]:
        assert find_adjacent_sum(data) == answer
    data = int(list(utils.get_data(3))[0].strip())
    first = find_adjacent_sum(data)
    print(f'Part 2: {first}')
