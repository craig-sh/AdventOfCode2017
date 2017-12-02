import utils

data = utils.get_data(1)
datalen = len(data)

counter = sum(int(x) for i, x in enumerate(data)
              if x == data[(i + 1) % datalen])
print(f'Part 1: {counter}')

look_ahead = int(datalen / 2)
counter = sum(int(x) for i, x in enumerate(data)
              if x == data[(i + look_ahead) % datalen])
print(f'Part 2: {counter}')
