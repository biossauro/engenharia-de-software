from unittest import TestCase
from src.stack import Stack


class TestStack(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_push(self):
        self.stack.push(2)
        self.assertFalse(self.stack.is_empty())

    def test_pop(self):
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        self.stack.push(4)
        self.assertEqual(self.stack.peek(), 4)
        self.assertFalse(self.stack.is_empty())

    def test_size(self):
        self.stack.push(5)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(6)
        self.assertEqual(self.stack.size(), 2)
