from utils import utils

cleansed = [raw_line.split() for raw_line in utils.get_data(4)]
valid_count = sum(1 for line in cleansed
                  if len(line) == len(set(line)))
print(f'Part 1: {valid_count}')


cleansed = [[''.join(sorted(x)) for x in line.split()]
            for line in utils.get_data(4)]
valid_count = sum(1 for line in cleansed
                  if len(line) == len(set(line)))
print(f'Part 2: {valid_count}')
