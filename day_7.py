from utils import utils
from typing import Dict, List
from collections import namedtuple, Counter

Element = namedtuple('Element', ['name', 'number', 'children'])
elements: Dict[str, Element] = {}
has_parents = set()
for line in utils.get_data(7):
    data = line.split()
    name = data[0]
    number = int(data[1].strip('()'))
    children: List = []
    if len(data) > 2:
        children = [x for x in [i.strip(',').strip() for i in data[3:]] if x]
    has_parents.update(children)
    elements[name] = Element(name, number, children)

root = next(iter(set(elements.keys()) - has_parents))
print(f'Part 1: {root}')


def calculate_weight(element):
    weights = {x: calculate_weight(elements[x]) for x in element.children}
    if weights:
        counts = Counter(weights.values())
        if len(counts) > 1:
            sorted_count = sorted(counts.items(), key=lambda x: x[1])
            bad_weight = sorted_count[0][0]
            good_weight = sorted_count[1][0]
            bad_elem = None
            for x in weights:
                if bad_weight == weights[x]:
                    bad_elem = elements[x]
                    break
            bad_elem_children_total_weight = bad_weight - bad_elem.number
            necessary_weight = good_weight - bad_elem_children_total_weight
            raise ValueError('Unbalanced', necessary_weight)
    return element.number + sum(weights.values())


try:
    calculate_weight(elements[root])
except ValueError as ve:
    print(f'Part 2: {ve.args[1]}')
