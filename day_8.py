from utils import utils
from typing import List
from collections import defaultdict


ulti_max = 0
d: defaultdict = defaultdict(int)
for line in utils.get_data(8):
    chars: List[str] = line.split()
    cond: bool = bool(eval(str(d[chars[4]]) + ' ' + ' '.join(chars[5:])))
    if cond:
        if chars[1] == 'inc':
            d[chars[0]] += int(chars[2])
        else:
            d[chars[0]] -= int(chars[2])
    ulti_max = max(d[chars[0]], ulti_max)

max_ = max(d.values())

print(f'Part 1: {max_}')
print(f'Part 2: {ulti_max}')
