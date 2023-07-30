"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest

from src.queue import Node, Queue


class NodeTestCase(unittest.TestCase):
    def test_node_creation(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)

        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')

class QueueTestCase(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()

        queue.enqueue('data1')
        self.assertEqual(queue.head.data, 'data1')
        self.assertIs(queue.head, queue.tail)

        queue.enqueue('data2')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')

        queue.enqueue('data3')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.head.next_node.next_node.data, 'data3')

    def test_dequeue(self):
        queue = Queue()

        self.assertIsNone(queue.dequeue())

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.head.data, 'data2')

        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.head.data, 'data3')

        self.assertEqual(queue.dequeue(), 'data3')

        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

        self.assertIsNone(queue.dequeue())



    def test_str(self):
        queue = Queue()
        self.assertEqual(str(queue), "")
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(str(queue), "data1\ndata2\ndata3")