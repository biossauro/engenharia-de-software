from abc import ABC, abstractmethod
from src.observer_interface import ObserverInterface


class SubjectInterface(ABC):
    @abstractmethod
    def notify_observers(self) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: ObserverInterface) -> None:
        pass

    @abstractmethod
    def register_observer(self, observer: ObserverInterface) -> None:
        pass
