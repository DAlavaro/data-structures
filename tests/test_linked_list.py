"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class NodeTestCase(unittest.TestCase):
    def test_node_creation(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)

        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')





class LinkedListTestCase(unittest.TestCase):

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(str(ll), "{'id': 1} -> None")

        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> None")

    def test_insert_at_end(self):
        ll = LinkedList()

        ll.insert_at_end({'id': 1})
        self.assertEqual(str(ll), "{'id': 1} -> None")

        ll.insert_at_end({'id': 2})
        self.assertEqual(str(ll), "{'id': 1} -> {'id': 2} -> None")

    def test_str(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})

        a = "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"

        # Печатаем данные
        self.assertEqual(str(ll), a)