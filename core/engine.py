import time
import logging

from core.scene import GameObject, Scene
from threading import Thread

PAUSE = 'PAUSE'
PLAY = 'PLAY'
STOP = 'STOP'


class Engine(Thread):
    def __init__(self, scene: Scene, fps=60) -> None:
        self.logger = logging.Logger(
            self.__class__.__name__, level=logging.WARN)
        self.status = PAUSE
        self.scene = scene
        self.fps = fps

        Thread.__init__(self, group=None, target=self.start,
                        name='cli_engine', args=self, kwargs=None, daemon=None)

    def run(self) -> None:
        return self._start()

    def _start(self):
        self.status = PLAY
        while self.status == PLAY:
            self.update()
            time.sleep(1/self.fps)

    def stop(self):
        self.status = STOP

    def update(self):
        self.logger.info('update function called.')
        self._update_per_frame()
        self._detect_collision()
        self._draw_frame()

    def _update_per_frame(self):
        game_objects = self.scene.objects
        for game_object in game_objects.values():
            game_object.update()
        self.logger.info('frame updated.')

    def _detect_collision(self):
        def is_intersected(o1: GameObject, o2: GameObject) -> bool:
            o1_left, o1_right = o1.position.x, o1.position.x + o1.dimension.width
            o1_top, o1_down = o1.position.y, o1.position.y + o1.dimension.height

            o2_left, o2_right = o2.position.x, o2.position.x + o2.dimension.width
            o2_top, o2_down = o2.position.y, o2.position.y + o2.dimension.height

            is_x_axis_intersected = o1_right <= o2_left or o2_right <= o1_left
            is_y_axis_intersected = o1_top <= o2_down or o2_top <= o1_down
            return not (is_x_axis_intersected or is_y_axis_intersected)

        game_objects = list(self.scene.objects.values())
        for i in range(len(game_objects)):
            o1 = game_objects[i]
            for j in range(i+1, len(game_objects)):
                o2 = game_objects[j]
                if is_intersected(o1, o2):
                    self.logger.info('collision detected between, o1= %s, o2= %s' % (
                        o1.__name__, o2.__name__))
                    o1.collide(o2)
                    o2.collide(o1)

    def _draw_frame(self):
        self.scene.draw()
