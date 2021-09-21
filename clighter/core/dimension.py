class Dimension:
    def __init__(self, height: int, width: int) -> None:
        """
        Construct dimension object.
        Dimension is useful when you deal with scene.
        `height` can be seen as the distance from the starting point of some `y` point
        in coordinate system.
        `width` can be seen as the distance from the starting point of some `x` point 
        in coordinate system. 
        """
        self.height = height
        self.width = width
