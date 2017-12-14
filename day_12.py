from utils import utils
from collections import deque


PID_MAP = {}
for line in utils.get_data(12):
    cleansed = line.split(' <-> ')
    pid = int(cleansed[0])
    comms = [int(x.strip()) for x in cleansed[1].split(',') if x.strip()]
    PID_MAP[pid] = comms


def find_links(root_pid):
    observed = set([root_pid])
    todo = deque([root_pid])
    while todo:
        pid = todo.pop()
        for next_pid in PID_MAP[pid]:
            if next_pid not in observed:
                observed.add(next_pid)
                todo.append(next_pid)
    return observed


def find_groups():
    remaining = set(PID_MAP.keys())
    groups = deque()
    while remaining:
        next_pid = remaining.pop()
        cur_group = find_links(next_pid)
        remaining -= cur_group
        groups.append(cur_group)
    return groups


observed = find_links(0)
print(f'Part 1: {len(observed)}')

groups = find_groups()
print(f'Part 2: {len(groups)}')
