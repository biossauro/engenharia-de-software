from unittest import TestCase
from src.bubble_sort import BubbleSort


class TestBubbleSort(TestCase):
    def test_bubble_sort(self):
        array_list = [5, 4, 3, 2, 1]
        new_array_list = BubbleSort.sort(array_list)
        self.assertEqual(new_array_list, [1, 2, 3, 4, 5])
