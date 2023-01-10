from threading import Event, Semaphore, Thread
from src.timer import Timer


class ThreadController:
    def __init__(self):
        self.event = Event()
        self.semaphore = Semaphore()
        self.counter = 0

    def new_timer(self, time, use_semaphore=False):
        if self.event.is_set():
            self.event.clear()
        thread = Thread(target=self.__create_timer, args=(time, use_semaphore))
        thread.start()

    def __create_timer(self, time, use_semaphore):
        self.counter += 1
        if not use_semaphore:
            Timer(self.counter, time, self.event)
        else:
            try:
                self.semaphore.acquire()
                Timer(self.counter, time, self.event)
            finally:
                self.semaphore.release()

    def stop(self):
        self.event.set()
