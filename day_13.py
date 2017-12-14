from utils import utils
from itertools import dropwhile, count


FIREWALL = {}
for line in utils.get_data(13):
    cleansed = [int(x.strip()) for x in line.split(':') if x.strip()]
    FIREWALL[cleansed[0]] = cleansed[1]
TOTAL_TIME = max(FIREWALL.keys())


def move(start_time):
    for t in range(start_time, start_time + TOTAL_TIME + 1):
        range_ = FIREWALL.get(t - start_time)
        if range_ and t % (range_ + range_ - 2) == 0:
            yield range_ * (t - start_time)


def get_severity(start_time):
    return sum(x for x in move(start_time))


severity = get_severity(0)
print(f'Part 1: {severity}')

escape_nums = dropwhile(lambda x: any(i is not None for i in move(x)), count())
print(f'Part 2: {next(escape_nums)}')
