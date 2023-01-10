from unittest import TestCase
from src.quick_sort import QuickSort


class TestQuickSort(TestCase):
    def test_merge_sort(self):
        array_list = [5, 4, 3, 2, 1]
        new_array_list = QuickSort.sort(array_list)
        self.assertEqual(new_array_list, [1, 2, 3, 4, 5])
