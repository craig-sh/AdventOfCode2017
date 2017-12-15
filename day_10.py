from utils import utils
from math import ceil
from functools import reduce
from itertools import repeat, chain
from operator import xor


STANDARD_SUFFIX = [17, 31, 73, 47, 23]
NUM_ROUNDS = 64
COUNT = 256


data = list(utils.get_data(10))[0]


def reverse_(list_, start_pos, end_pos):
    num_swaps = ceil((end_pos - start_pos) / 2)
    end_mod = end_pos % len(list_)
    for i in range(num_swaps):
        start_mod = (start_pos + i) % len(list_)
        end = (end_mod - i) % len(list_)
        list_[start_mod], list_[end] = list_[end], list_[start_mod]


def apply_knot(list_, lengths, num_rounds=1):
    skip_size = position = 0
    for length in chain.from_iterable(repeat(lengths, num_rounds)):
        reverse_(list_, position, position + length - 1)
        position += length + skip_size
        skip_size += 1


def get_knot_hash(value: str):
    lengths = [ord(x) for x in value if x]
    lengths += STANDARD_SUFFIX
    list_ = list(range(COUNT))
    apply_knot(list_, lengths, num_rounds=64)
    dense = [reduce(xor, list_[n: n + 16])
             for n in range(0, COUNT, 16)]
    hexes = [f'{x:02x}' for x in dense]
    output = ''.join(hexes)
    return output


def part_1():
    comma_sep = data.split(',')
    lengths = [int(x.strip()) for x in comma_sep if x.strip()]
    list_ = list(range(COUNT))
    apply_knot(list_, lengths)
    score = list_[0] * list_[1]
    print(f'Part 1: {score}')


def part_2():
    value = [x.strip() for x in data if x.strip()]
    output = get_knot_hash(value)
    print(f'Part 2: {output}')


if __name__ == '__main__':
    part_1()
    part_2()
