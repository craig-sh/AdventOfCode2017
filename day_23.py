from utils import utils
from typing import List
from collections import defaultdict, deque


class Processor():
    def __init__(self, pid: int, instr: List[str]) -> None:
        self.instr = instr
        self.registers = defaultdict(int)
        self.instr_pointer = 0
        self.mul_count = 0
        self.iternum = 0

    def execute(self):
        while True:
            raw = self.instr[self.instr_pointer]
            split = [x.strip() for x in raw.split() if x.strip()]
            cmd, args = split[0], split[1:]
            func = getattr(self, f'_{cmd}')
            func(args)
            self.instr_pointer += 1
            if self.instr_pointer in [29, 31]:
                print('hi')

            self.iternum += 1
            if self.instr_pointer < 0 or self.instr_pointer >= len(self.instr):
                raise Exception('Im done')
            if self.iternum % 500000 == 0:
                print(f'....{self.mul_count}')
            yield
        return

    def _get(self, arg):
        try:
            return int(arg)
        except ValueError:
            return self.registers[arg]

    def _set(self, args):
        self.registers[args[0]] = self._get(args[1])

    def _add(self, args):
        self.registers[args[0]] += self._get(args[1])

    def _sub(self, args):
        self.registers[args[0]] += self._get(args[1])

    def _mul(self, args):
        self.mul_count += 1
        self.registers[args[0]] *= self._get(args[1])

    def _jnz(self, args):
        if self._get(args[0]) != 0:
            # Jump 1 less because we always increment pointer after loop
            self.instr_pointer += self._get(args[1]) - 1



def main():
    data = list(utils.get_data(23))
    proc0 = Processor(0, data)
    p0 = proc0.execute()
    try:
        while True:
            next(p0)
    except Exception as e:
        print(e)
        print(p0.mul_count)
        print(p0.iternum)


if __name__ == '__main__':
    main()
