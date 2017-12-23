from utils import utils
from utils.euclidean import Point, COUNTER_CLOCKWISE, NORTH

def turn_left(direction):
    i = COUNTER_CLOCKWISE.index(direction)
    return  COUNTER_CLOCKWISE[(i + 1) % len(COUNTER_CLOCKWISE)]

def turn_right(direction):
    i = COUNTER_CLOCKWISE.index(direction)
    return COUNTER_CLOCKWISE[i - 1]

def turn_around(direction):
    i = COUNTER_CLOCKWISE.index(direction)
    return COUNTER_CLOCKWISE[i - 2]


def burst(location, infected):
    direction = NORTH
    total_infected = 0

    while True:
        # import ipdb;ipdb.set_trace()
        if location in infected:
            direction = turn_right(direction)
        else:
            direction = turn_left(direction)
        if location not in infected:
            infected.add(location)
            total_infected += 1
        else:
            infected.discard(location)
        location += direction
        yield total_infected

def is_in(x, checks):
    return any(x in check for check in checks)

def get_in(x, checks):
    for check in checks:
        if x in check:
            return check

def advanced_burst(location, infected):
    direction = NORTH
    total_infected = 0
    flagged = set()
    weakened = set()

    while True:
        if location in weakened:
            # direction is the same
            weakened.discard(location)
            infected.add(location)
            total_infected += 1
        elif location in infected:
            infected.discard(location)
            flagged.add(location)
            direction = turn_right(direction)
        elif location in flagged:
            flagged.discard(location)
            direction = turn_around(direction)
        else:
            direction = turn_left(direction)
            weakened.add(location)
        location += direction
        yield total_infected

        
def main():
    infected = set()
    height = 0
    width = 0
    for y, line in enumerate(utils.get_data(22)):
        if not line.strip():
            continue
        height += 1
        width = len(line.strip())
        for x, val in enumerate(line.strip()):
            if val == '#':
                infected.add(Point(x, y))
    mid = Point(width // 2, height // 2)
    print(f'Mid is {mid}')
    total_infected = 0
    burst_sim = burst(mid, infected.copy())
    for _ in range(10000):
        total_infected = next(burst_sim)
    print(f'Part 1: {total_infected}')

    burst_sim = advanced_burst(mid, infected)
    for _ in range(10000000):
        total_infected = next(burst_sim)
    print(f'Part 2: {total_infected}')

if __name__ == '__main__':
    main()
