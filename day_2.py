from utils import utils

cleansed = [utils.tab_split(raw_line, int) for raw_line in utils.get_data(2)]

checksum = sum(max(line) - min(line) for line in cleansed)
print(f'Part 1: {checksum}')


def find_divisor(line):
    """ Only 2 elements on each line will be divisible """
    sorted_line = sorted(line, reverse=True)
    for i, numerator in enumerate(sorted_line):
        for denominator in sorted_line[i + 1:]:
            if numerator % denominator == 0:
                return numerator // denominator


checksum = sum(find_divisor(x) for x in cleansed)
print(f'Part 2: {checksum}')
