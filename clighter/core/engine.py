import time

from threading import Thread

from .scene import Scene

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
        objects = list(self.scene.objects.values())
        objects.sort(key=lambda x: x.z_index)
        self._update_per_frame(objects)
        self._detect_collision(objects)
        self._draw_frame()

    def _update_per_frame(self, objects):
        for game_object in objects:
            game_object._update()

    def _detect_collision(self, objects):
        for i in range(len(objects)):
            o1 = objects[i]
            if o1.z_index < 0 or not o1.trigger_collision:
                continue
            for j in range(i+1, len(objects)):
                o2 = objects[j]
                if o1.z_index == o2.z_index and o1.rect().intersect(o2.rect()):
                    o1.collide(o2)
                    o2.collide(o1)

    def _draw_frame(self):
        self.scene.draw()
