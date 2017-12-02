# -*- coding: utf-8 -*-
""" Various utilities for solving challenges """

import os


def get_data(day_num: int) -> str:
    """Return current days data"""
    data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
    with open(os.path.join(data_dir, f'day_{day_num}.txt'), 'r') as fname:
        return fname.read()
