from utils import utils
from typing import Dict, Tuple, List


# Single tab deliminated line of input
config: List[int] = [utils.tab_split(x, int) for x in utils.get_data(6)][0]

# This will store each unique config, and which step
# it was encountered on
encountered_configs: Dict[Tuple, int] = {}
count = 0
while tuple(config) not in encountered_configs:
    encountered_configs[tuple(config)] = count

    highest_value = max(config)
    highest_bank = config.index(highest_value)

    config[highest_bank] = 0
    for i in range(highest_value):
        config[(highest_bank + i + 1) % len(config)] += 1

    count += 1

print(f'Part 1: {count}')
print(f'Part 2: {count - encountered_configs[tuple(config)]}')
