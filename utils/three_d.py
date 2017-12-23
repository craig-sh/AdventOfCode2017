class ThreeDPoint:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: 'ThreeDPoint') -> 'ThreeDPoint':
        return ThreeDPoint(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'ThreeDPoint') -> 'ThreeDPoint':
        return ThreeDPoint(self.x - other.x, self.y - other.y, self.z - other.z)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.z})'

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def dot(self, val):
        if isinstance(val, ThreeDPoint):
            return ThreeDPoint(self.x * val.x, self.y * val.y, self.z * val.z)
        return ThreeDPoint(self.x * val, self.y * val, self.z * val)
