"""
Clighter is a game engine built for command line games.
"""
from .cli import CLIGame, CLIScene, CLIInputChannel
from .core import (Position, Dimension, AnimationFrame, AnimationMixin,
                   GameObjectFactory, GameObject, Rectangle, Scene,
                   Engine, Game, InputChannel)

__all__ = ['CLIGame', 'CLIScene', 'CLIInputChannel', 'Position', 'Dimension',
           'AnimationFrame', 'AnimationMixin', 'GameObjectFactory',
           'GameObject', 'Rectangle', 'Scene', 'Engine', 'Game', 'InputChannel']
