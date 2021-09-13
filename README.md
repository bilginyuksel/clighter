# Clighter

__Clighter__ is a game engine for terminal games. You can use this library to build none flickering, totaly fluid games. You have very easy to use APIs in your hand with __clighter__.

When you use __clighter__ you don't have to think about how to render objects with multiple characters, you also don't need to think about the collision between objects and many other features that __clighter__ provides you. 

## Quick Start

### 1. Installation

- Install with pip 


```bash
$ pip install clighter
```

- Clone the library use without installation

```bash
$ git clone https://github.com/bilginyuksel/clighter
$ cd clighter/examples
$ mkdir <your-folder>
$ cd <your-folder>
```

After you execute the commands above you can create your own structure for your game. 

> NOTE: Do not forget to import sys and append to the directory where clighter exist. Follow the example code block to use the clighter package effectively for your project under `examples` directory.

```python
# This code is a must if you create your game under examples directory and if you want to use the local clighter package from that directory.
import sys
sys.path.append('../..')

# Then you can import the clighter
import clighter
# or 
from clighter import * # to use all classes and functions without clighter prefix
```

### 2. Usage

Render a character to the scene and subscribe character to input channel. Whenever user enters `w,a,s,d` the character will move to the given direction.

Also we need a character, you can copy the `character.txt` file from `clighter/examples/main/assets/character.txt` or you can create a brand new character for yourself. Be sure to give correct filepath.

```python
from clighter import CLIGame, GameObject, Position

class Character(GameObject):
    def __init__(self, position: Position) -> None:
        super().__init__(position, None, filepath='assets/character.txt',
                         obstacle=False, controllable=True)

    def on_key_pressed(self, key: chr):
        if key == 's':
            self.position.y += 3
        elif key == 'w':
            self.position.y -= 3
        elif key == 'd':
            self.position.x += 3
        elif key == 'a':
            self.position.x -= 3

if __name__ == '__main__':
    game = CLIGame()
    factory = GameObjectFactory()
    character = Character(Position(10, 10))
    # channel=True and scene=True means character will be put to scene and subscribe to channel
    factory.put(character, channel=True, scene=True)
    game.start()
```

## Some of the features

### Rendering

__Clighter__ will automatically handle object rendering. You just need to provide a `.txt` file to the game object. After you give the filepath to the object it will automatically render it without a problem. 

Also you can move the character without having any rendering problems at all. Just change the position of the object and it will move. 

```python
class SomeObject(GameObject):
    ...
    ...

    def update(self):
        # the object will move at x_axis by 1 unit in every frame.
        self.position.x += 1
    
    ...
    ...

```


### Collision

Collision is a very important and good feature when you create games. With __clighter__ you can create layered rendering hierarcy between the objects with the `z_index`. When you put some objects in the same `z_index` whenever they collide with each other the engine will automatically trigger their `collide` functions. 

> NOTE: If there are a lot objects in the scene then calculating collision for every object will be a lot of work but good news: you can simply optimize it via using a single parameter. For instance if there are a lot of bullets in the map then the system will control the collision effect between bullets and character both at the same time. But you can deactivate the bullet collision search and the game will be much more faster.

```python
class Bullet(GameObject):

    def __init__(self):
        # When you set `trigger_collision` parameter to False the engine will skip collision effect for bullet. But that does not mean you will miss this collision effect. If this bullet collides with a character you can catch the collision effect with the character's collide function.
        GameObject.__init__(self, position, dimension=None, filepath=None,
                            obstacle=False, controllable=False, trigger_collision=False)

    # if `trigger_collision` parameter is False then the function below will not be triggered even if there is a collision but if this bullet object collides with another object and if the collided objects `trigger_colision` parameter is True then the collision effect can be captured with collided object's collide function.
    def collide(self, obj: GameObject):
        pass
```
