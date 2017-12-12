# -*- coding: utf-8 -*-
""" Various utilities for solving challenges """

import os
from typing import Callable, List, Any, Generator


def get_data(day_num: int) -> Generator[str, None, None]:
    """Return data for day. Assumes data files are in ../data/"""
    data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            '..', 'data')
    with open(os.path.join(data_dir, f'day_{day_num}.txt'), 'r') as fobj:
        yield from fobj


def get_single_line_split(day_num: int, split_char: str) -> Generator[str, None, None]:
    for line in get_data(day_num):
        for elem in line.split(split_char):
            clean = elem.strip()
            if clean:
                yield clean


def tab_split(line: str, converter: Callable[[str], Any]=str) -> List[Any]:
    """Split a line by tabs and convert each element"""
    return [converter(x) for x in line.split('\t')]
