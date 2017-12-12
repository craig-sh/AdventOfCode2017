class HexPoint:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: 'HexPoint') -> 'HexPoint':
        return HexPoint(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'HexPoint') -> 'HexPoint':
        return HexPoint(self.x - other.x, self.y - other.y, self.z - other.z)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.z})'

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def distance(self, other):
        dist = self - other
        return max(abs(c) for c in [dist.x, dist.y, dist.z])


class HexVector(HexPoint):
    pass


NORTH = HexVector(0, 1, -1)
SOUTH = HexVector(0, -1, 1)
NORTH_WEST = HexVector(-1, 1, 0)
SOUTH_WEST = HexVector(-1, 0, 1)
NORTH_EAST = HexVector(1, 0, -1)
SOUTH_EAST = HexVector(1, -1, 0)
