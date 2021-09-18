import unittest
from deque import Deque


class TestDeque(unittest.TestCase):

    def test_insert_front(self):
        my_deque = Deque()
        my_deque.insert_front(34)
        my_deque.insert_front(56)
        my_deque.insert_front(78)
        my_deque.insert_front(89)
        my_deque = my_deque.deque_to_list()
        self.assertEqual(my_deque, [89, 78, 56, 34])

    def test_insert_last(self):
        my_deque = Deque()
        my_deque.insert_last(34)
        my_deque.insert_last(56)
        my_deque.insert_last(78)
        my_deque.insert_last(89)
        my_deque = my_deque.deque_to_list()
        self.assertEqual(my_deque, [34, 56, 78, 89])

    def test_delete_front(self):
        my_deque = Deque()
        my_deque.insert_last(34)
        my_deque.insert_last(56)
        my_deque.insert_last(78)
        my_deque.insert_last(89)
        my_deque.delete_front()
        my_deque = my_deque.deque_to_list()
        self.assertEqual(my_deque, [56, 78, 89])

    def test_delete_last(self):
        my_deque = Deque()
        my_deque.insert_front(34)
        my_deque.insert_front(56)
        my_deque.insert_front(78)
        my_deque.insert_front(89)
        my_deque.delete_last()
        my_deque = my_deque.deque_to_list()
        self.assertEqual(my_deque, [89, 78, 56])

    def test_get_front(self):
        my_deque = Deque()
        my_deque.insert_front(34)
        my_deque.insert_front(56)
        my_deque.insert_front(78)
        my_deque.insert_front(89)
        self.assertEqual(my_deque.get_front(), 89)

    def test_get_last(self):
        my_deque = Deque()
        my_deque.insert_front(34)
        my_deque.insert_front(56)
        my_deque.insert_front(78)
        my_deque.insert_front(89)
        self.assertEqual(my_deque.get_last(), 34)
