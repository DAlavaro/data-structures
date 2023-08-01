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

    def setUp(self):
        # Создаем связанный список и добавляем несколько узлов для каждого теста
        self.ll = LinkedList()
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})

    def test_to_list(self):
        # Тестирование метода to_list()
        data_list = self.ll.to_list()
        self.assertEqual(data_list,
                         [{'id': 0, 'username': 'serebro'}, {'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}])

    def test_get_data_by_id_existing(self):
        # Тестирование метода get_data_by_id() с существующим id
        kid = 2
        data_by_id = self.ll.get_data_by_id(kid)
        self.assertEqual(data_by_id, {'id': 2, 'username': 'mik.roz'})

    def test_get_data_by_id_non_existing(self):
        # Тестирование метода get_data_by_id() с несуществующим id
        target_id = 4
        data_by_id = self.ll.get_data_by_id(target_id)
        self.assertIsNone(data_by_id)
