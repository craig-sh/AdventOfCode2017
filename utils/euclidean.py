class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


class Vector(Point):
    pass


class Grid:
    def __init__(self, grid):
        self.grid = grid

    def __getitem__(self, key):
        if isinstance(key, Point):
            return self.grid[key.y][key.x]
        return self.grid[key]

    def get(self, point, default=None):
        try:
            return self.__getitem__(point)
        except IndexError:
            return default

NORTH = Vector(0, -1)
SOUTH = Vector(0, 1)
EAST = Vector(1, 0)
WEST = Vector(-1, 0)
NORTH_WEST = Vector(1, -1)
NORTH_EAST = Vector(1, 1)
SOUTH_WEST = Vector(-1, -1)
SOUTH_EAST = Vector(-1, 1)

COUNTER_CLOCKWISE = [EAST, NORTH, WEST, SOUTH]
DIAG = [
    NORTH, NORTH_WEST, WEST, SOUTH_WEST,
    SOUTH, SOUTH_EAST, EAST, NORTH_EAST,
]
