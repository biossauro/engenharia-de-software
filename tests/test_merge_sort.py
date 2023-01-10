from unittest import TestCase
from src.merge_sort import MergeSort


class TestMergeSort(TestCase):
    def test_merge_sort(self):
        array_list = [5, 4, 3, 2, 1]
        new_array_list = MergeSort.sort(array_list)
        self.assertEqual(new_array_list, [1, 2, 3, 4, 5])
