# -*- coding: utf-8 -*-
""" Various utilities for solving challenges """

import os
from typing import Callable, List, Any, Generator


def get_data(day_num: int) -> Generator[str, None, None]:
    """Return current days data"""
    data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
    with open(os.path.join(data_dir, f'day_{day_num}.txt'), 'r') as fobj:
        yield from fobj


def tab_split(line: str, converter: Callable[[str], Any]=str) -> List[Any]:
    """Split a line by tabs and convert each element"""
    return [converter(x) for x in line.split('\t')]
