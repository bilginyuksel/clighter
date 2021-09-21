from .dimension import Dimension
from .position import Position


class Rectangle:
    def __init__(self, position: Position, dimension: Dimension) -> None:
        """
        Construct rectangle object from `position` and `dimension`. 
        """
        self.left = position.x
        self.right = position.x + dimension.width
        self.top = position.y
        self.bottom = position.y + dimension.height

    def intersect(self, other) -> bool:
        """
        Intersect check whether the `self` rectangle and `other` rectangle is intersected  
        """
        return not (other.left > self.right or other.right < self.left or other.top > self.bottom or other.bottom < self.top)

    def __str__(self) -> str:
        return 'l= %d, r=%d, t= %d, b= %d' % (self.left, self.right, self.top, self.bottom)
