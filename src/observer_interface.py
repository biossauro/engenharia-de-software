from abc import ABC, abstractmethod


class ObserverInterface(ABC):
    @abstractmethod
    def update(self) -> None:
        pass
