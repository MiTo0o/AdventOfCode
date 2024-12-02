import numpy
from functools import total_ordering, reduce
import math

def print_grid(lst):
    for i in lst:
        print(i)
    
def prefix_sum(lst):
    numpy.cumsum(lst)
    
def unique(lst):
    return len(lst) == len(set(lst))



class Point:
    
    def __init__(self, x, y) -> None:
        self.X = x
        self.Y = y
        
    def neighbor_4(self) -> None:
        return []
        
    def __hash__(self):
        return hash(tuple((self.X, self.Y)))
    
    def __ne__(self, other: object) -> bool:
        return not self == other
    
    def __eq__(self, other: object) -> bool:
        return self.X == other.X and self.Y == other.Y
    
    def __repr__(self) -> str:
        return f'Point({self.X}, {self.Y})'
    
    def __str__(self) -> str:
        return f'({self.X}, {self.Y})'

    def __add__(self, other):
        return Point(self.X + other.X, self.Y + other.Y)
        
    def __sub__(self, other):
        return Point(self.X - other.X, self.Y - other.Y)

    def __mul__(self, n):
        return Point(self.X * n, self.Y * n)

    def __div__(self, n):
        return Point(self.X / n, self.Y / n)

    def __neg__(self):
        return Point(-self.X, -self.Y)

    @property
    def neighbors_4(self) -> list:
        return [self + p for p in DIRS_4]

    @property
    def neighbors_8(self) -> list:
        return [self + p for p in DIRS_8]

    @property
    def length(self):
        return math.sqrt(self.X ** 2 + self.Y ** 2)


N = Point(0, 1)
NE = Point(1, 1)
E = Point(1, 0)
SE = Point(1, -1)
S = Point(0, -1)
SW = Point(-1, -1)
W = Point(-1, 0)
NW = Point(-1, 1)

DIRS_4 = [
    Point(0, 1),   # north
    Point(1, 0),   # east
    Point(0, -1),  # south
    Point(-1, 0),  # west
]

DIRS_8 = [
    Point(0, 1),    # N
    Point(1, 1),    # NE
    Point(1, 0),    # E
    Point(1, -1),   # SE
    Point(0, -1),   # S
    Point(-1, -1),  # SW
    Point(-1, 0),   # W
    Point(-1, 1),   # NW
]

