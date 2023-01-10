from typing import List
from src.observer import ObserverInterface
from src.subject_interface import SubjectInterface


class Subject(SubjectInterface):
    def __init__(self):
        self.__observers: List[ObserverInterface] = []
        self.__phrase: str = ""

    @property
    def phrase(self) -> str:
        return self.__phrase

    @phrase.setter
    def phrase(self, phrase: str) -> None:
        self.__phrase = phrase
        self.notify_observers()

    @phrase.getter
    def get_phrase(self) -> str:
        return self.__phrase

    def split_phrase(self) -> list:
        return self.__phrase.split()

    def count_words(self) -> int:
        return len(self.split_phrase())

    def count_capital_words(self) -> int:
        return len([word for word in self.split_phrase() if word[0].isupper()])

    def notify_observers(self) -> None:
        for observer in self.__observers:
            observer.update(self.__phrase)

    def register_observer(self, observer: ObserverInterface) -> None:
        self.__observers.append(observer)

    def remove_observer(self, observer: ObserverInterface) -> None:
        self.__observers.remove(observer)

    def get_observers(self) -> list:
        return self.__observers
