from src.sorting_algorithm import SortingAlgorithm


class MergeSort(SortingAlgorithm):
    @classmethod
    def sort(cls, array_list: list) -> list:
        new_array_list = cls.sorting.mergeSort(array_list)
        return new_array_list
