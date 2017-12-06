from utils import utils

cleansed = [int(x) for x in utils.get_data(5)]

pos = count = 0
while pos < len(cleansed):
    pos, old_pos = pos + cleansed[pos], pos
    cleansed[old_pos] += 1
    count += 1
print(f'Part 1: {count}')

cleansed = [int(x) for x in utils.get_data(5)]

pos = count = 0
while pos < len(cleansed):
    jump = cleansed[pos]
    pos, old_pos = pos + cleansed[pos], pos
    cleansed[old_pos] += -1 if cleansed[old_pos] >= 3 else 1
    count += 1
print(f'Part 2: {count}')
