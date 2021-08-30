from core.animation import AnimationMixin
import time

from core.scene import Scene
from threading import Thread

PAUSE = 'PAUSE'
PLAY = 'PLAY'
STOP = 'STOP'


class Engine(Thread):
    def __init__(self, scene: Scene, fps=60) -> None:
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
        self._update_per_frame()
        self._detect_collision()
        self._draw_frame()

    def _update_per_frame(self):
        objects = list(self.scene.objects.values())
        for game_object in objects:
            game_object._update()

    def _detect_collision(self):
        objects = list(self.scene.objects.values())
        for i in range(len(objects)):
            o1 = objects[i]
            for j in range(i+1, len(objects)):
                o2 = objects[j]
                if o1.rect().intersect(o2.rect()):
                    o1.collide(o2)
                    o2.collide(o1)

    def _draw_frame(self):
        self.scene.draw()
