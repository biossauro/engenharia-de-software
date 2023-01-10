from src.observer_interface import ObserverInterface


class Observer(ObserverInterface):
    def __init__(self, phrase: str):
        self.__phrase: str = phrase

    def update(self, phrase: str):
        self.__phrase = phrase
