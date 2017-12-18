from utils import utils
from typing import List
from collections import defaultdict, deque


class Processor():
    def __init__(self, pid: int, instr: List[str]) -> None:
        self.pid = pid
        self.instr = instr
        self.registers = defaultdict(int)
        self.registers['p'] = self.pid
        self.last_played = None
        self.recovered = None
        self.instr_pointer = 0
        self.first_recovery = None
        self.send_queue = deque()
        self.other = None
        self.waiting = False
        self.num_sent = 0

    def set_other(self, p: 'Processor'):
        self.other = p

    def execute(self):
        while True:
            raw = self.instr[self.instr_pointer]
            split = [x.strip() for x in raw.split() if x.strip()]
            cmd, args = split[0], split[1:]
            func = getattr(self, f'_{cmd}')
            if cmd == 'rcv':
                yield from func(args)
            else:
                func(args)
            self.instr_pointer += 1
            if self.instr_pointer < 0 or self.instr_pointer >= len(self.instr):
                break
            yield
        return

    def _get(self, arg):
        try:
            return int(arg)
        except ValueError:
            return self.registers[arg]

    def _snd(self, args):
        val = self._get(args[0])
        self.last_played = val
        self.send_queue.append(val)
        self.num_sent += 1

    def _set(self, args):
        self.registers[args[0]] = self._get(args[1])

    def _add(self, args):
        self.registers[args[0]] += self._get(args[1])

    def _mul(self, args):
        self.registers[args[0]] *= self._get(args[1])

    def _mod(self, args):
        self.registers[args[0]] = self.registers[args[0]] % self._get(args[1])

    def _rcv(self, args):
        if self._get(args[0]) != 0:
            self.recovered = self.last_played
            if self.first_recovery is None:
                self.first_recovery = self.last_played
                print(f'Part 1: {self.last_played}')
        while not self.other.send_queue:
            yield
            self.waiting = True
            if self.other.waiting and not self.send_queue:
                raise Exception('Terminating')
        self.waiting = False
        self.registers[args[0]] = self.other.send_queue.popleft()

    def _jgz(self, args):
        if self._get(args[0]) > 0:
            # Jump 1 less because we always increment pointer after loop
            self.instr_pointer += self._get(args[1]) - 1


def main():
    data = list(utils.get_data(18))
    proc0 = Processor(0, data)
    proc1 = Processor(1, data)
    proc0.set_other(proc1)
    proc1.set_other(proc0)
    p0 = proc0.execute()
    p1 = proc1.execute()
    try:
        while True:
            next(p0)
            next(p1)
    except Exception as e:
        print(e)
        print(f'Part 2: {proc1.num_sent}')


if __name__ == '__main__':
    main()
