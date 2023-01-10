from queue import Queue
from threading import Event, Thread


class RoundRobin(Queue):
    def __init__(self, quantum=1):
        super().__init__()
        self._quantum = quantum
        self._count = 0
        self._event = Event()
        self._thread = Thread(target=self._run)
        self._thread.start()

    def add_process(self, burst_time):
        process = {
            "burst_time": burst_time,
            "id": self._count
        }
        self._count += 1
        self.put(process)

    def _run(self):
        while not self._event.isSet():
            if not self.empty():
                process = self.get()
                print(f"\nProcesso {process['id']} está rodando...")
                self._event.wait(self._quantum)
                process["burst_time"] -= self._quantum
                if process["burst_time"] > 0:
                    self.put(process)
                else:
                    print(f"Processo {process['id']} finalizado!")

    def stop(self):
        self._event.set()
