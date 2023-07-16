import unittest
from src.stack import Node, Stack


class NodeTestCase(unittest.TestCase):
    def test_node_creation(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)

        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')

class StackTestCase(unittest.TestCase):
    def test_stack_push(self):
        stack = Stack()

        stack.push('data1')
        self.assertEqual(stack.top.data, 'data1')

        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')

        stack.push('data3')
        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')

    def test_stack_pop(self):
        stack = Stack()

        self.assertIsNone(stack.pop())

        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        self.assertEqual(stack.pop(), 'data3')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.pop(), 'data2')
        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(stack.pop(), 'data1')
        self.assertIsNone(stack.top)
        self.assertIsNone(stack.pop())
