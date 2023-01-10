from src.sorting_algorithm import SortingAlgorithm


class QuickSort(SortingAlgorithm):
    @classmethod
    def sort(cls, array_list: list) -> list:
        low, high = 0, len(array_list) - 1
        new_array_list = cls.sorting.quickSort(array_list, low, high)
        return new_array_list
