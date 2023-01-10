from abc import abstractmethod
from sorting_techniques import pysort


class SortingAlgorithm:
    sorting = pysort.Sorting()

    @abstractmethod
    def sort(cls, array_list: list) -> list:
        pass
