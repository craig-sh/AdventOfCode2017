from utils import utils
import sys


sys.setrecursionlimit(5000)
data = list(utils.get_data(9))[0].strip()
garbage = 0


def get_score(stream, position=0, brace_count=1):
    # print(f'{brace_count}:{stream})')
    if position >= len(data) - 5:
        return 0
    if stream[position] == '{':
        return brace_count + get_score(stream, position + 1, brace_count + 1)
    elif stream[position] == ',':
        return get_score(stream, position + 1, brace_count)
    elif stream[position] == '}':
        return get_score(stream, position + 1, brace_count - 1)
    elif stream[position] == '<':
        new_position = skip_garbage(stream, position + 1)
        return get_score(stream, new_position, brace_count)
    else:
        print(stream[position])


def skip_garbage(stream, position):
    global garbage
    while stream[position] != '>':
        if stream[position] == '!':
            position += 2
        else:
            garbage += 1
            position += 1
    return position + 1


score = get_score(data)
print(f'Part 1: {score}')
print(f'Part 2: {garbage}')
