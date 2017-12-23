from utils import utils
import numpy as np
from itertools import chain


def make_tuple(matrix):
    return tuple(tuple(x) for x in matrix)


def get_rotates(matrix):
    for _ in range(3):
        matrix = list(zip(*matrix[::-1]))
        yield make_tuple(matrix)

def get_flips(matrix):
    dim = len(matrix)
    new = [[None] * dim for i in range(dim)]
    idim = dim - 1
    # vertical flip
    for y in range(dim):
        for x in range(dim):
            new[y][idim - x] = matrix[y][x]
    yield make_tuple(new)
    # horizontal flip
    for y in range(dim):
        for x in range(dim):
            new[idim - y][x] = matrix[y][x]
    yield make_tuple(new)
    # diag flip (transpose)
    for y in range(dim):
        for x in range(dim):
            new[x][y] = matrix[y][x]
    yield make_tuple(new)
    a = np.array(matrix)
    b = np.flip(a, 0)
    b = np.flip(b, 1)
    yield make_tuple(b.transpose())

def get_transform(matrix, transforms):
    check = chain.from_iterable([
                [matrix],
                get_flips(matrix),
                get_rotates(matrix)
            ])
    for m in check:
        t = make_tuple(m)
        if t in transforms:
            print('found')
            return transforms[t]
    import ipdb;ipdb.set_trace()
    raise Exception('Neeed to do the diagonal thing!!')


def enhance(matrix, transforms):
    dim = len(matrix)
    step = 2 if dim % 2 == 0 else 3
    def get_new():
        return [[None] * step for i in range(step)]

    steps =  list(range(dim))[::step]
    new_map = [[None] * len(steps) for i in range(len(steps))]
    for iy, y_pos in enumerate(steps):
        for ix, x_pos in enumerate(steps):
            new = get_new()
            for y in range(step):
                for x in range(step):
                    new[y][x] = matrix[y + y_pos][x + x_pos]
            trns = get_transform(new, transforms)
            new_map[iy][ix] = trns
    new_dim =  len(steps) * len(new_map[0][0])
    inner_dim = len(new_map[0][0])
    final_mat = [[None] * new_dim for i in range(new_dim)]
    for y in range(len(steps)):
        new_y = y * inner_dim
        for x in range(len(steps)):
            new_x = x * inner_dim
            for iy in range(inner_dim):
                for ix in range(inner_dim):
                    final_mat[new_y + iy][new_x + ix] = new_map[y][x][iy][ix]
    return final_mat

 

def main():
    transforms = {}
    for line in utils.get_data(21):
        line = line.split('=>')
        pattern = []
        for row in line[0].strip().split('/'):
            pattern.append(tuple([x for x in row]))
        transform = []
        for row in line[1].strip().split('/'):
            transform.append([x for x in row])
        transforms[tuple(pattern)] = transform
    raw_pattern = [
        '.#.',
        '..#',
        '###'
    ]
    matrix = [[x for x in pattern] for pattern in raw_pattern]
    # print(np.array(matrix))
    # for pattern in get_flips(matrix):
    #     print(np.array(pattern))


    for _ in range(18):
        matrix = enhance(matrix, transforms)
    c = 0
    for y in matrix:
        for x in y:
            if x == '#':
                c += 1
    print(c)
if __name__ == '__main__':
    main()
