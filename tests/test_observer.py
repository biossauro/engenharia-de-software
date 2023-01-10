from unittest import TestCase
from src.observer import Observer
from src.subject import Subject


class TestObserver(TestCase):
    def setUp(self):
        self.observer_1: Observer = Observer("Hello, world!")
        self.observer_2: Observer = Observer("This is a test. Only a test...")
        self.subject: Subject = Subject()
        self.phrase: str

    def test_register_observer(self):
        self.subject.register_observer(self.observer_1)
        self.assertTrue(self.observer_1 in self.subject.get_observers())

    def test_remove_observer(self):
        self.subject.register_observer(self.observer_1)
        self.subject.remove_observer(self.observer_1)
        self.assertFalse(self.observer_1 in self.subject.get_observers())
