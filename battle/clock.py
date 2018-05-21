import time

class Clock:

    def __init_(self, speed=1):
        self._current_time = 0
        self._speed = speed

    def tick(self):
        self._current_time += 1
        time.sleep(self._speed)

    def time(self):
        return self._current_time