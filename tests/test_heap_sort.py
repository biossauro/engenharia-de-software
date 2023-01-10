from unittest import TestCase
from src.heap_sort import HeapSort


class TestHeapSort(TestCase):
    def test_heap_sort(self):
        array_list = [5, 4, 3, 2, 1]
        new_array_list = HeapSort.sort(array_list)
        self.assertEqual(new_array_list, [1, 2, 3, 4, 5])
