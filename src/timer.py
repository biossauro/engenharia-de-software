from playsound import playsound as play


class Timer:
    def __init__(self, id, time, event):
        self.id = id
        self.__start(time, event)

    def __start(self, time, event):
        finished = False
        while not event.is_set() and not finished:
            print(f'Alarm {self.id}: {time}min left...\n')
            event.wait(INTERVAL)
            time -= 1
            finished = True if time == 0 else False
        if finished:
            print(f'Alarm {self.id} finished!\n')
            play('assets/zapzap.mp3')
        else:
            print(f'Alarm {self.id} interrupted!\n')


INTERVAL = 6  # in seconds
