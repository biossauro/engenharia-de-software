from src.sorting_algorithm import SortingAlgorithm


class BubbleSort(SortingAlgorithm):
    @classmethod
    def sort(cls, array_list: list) -> list:
        new_array_list = cls.sorting.bubbleSort(array_list)
        return new_array_list
