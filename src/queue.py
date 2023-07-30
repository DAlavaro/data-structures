class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """ Метод для добавления элемента в очередь """
        new_node = Node(data)
        if self.head is None:
            # Если очередь пуста добавляем новый элемент
            self.head = new_node
            self.tail = new_node
        else:
            # Иначе добавляем элемент в конец очереди
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """ Метод для удаления элемента из очереди. Возвращает данные удаленного элемента """
        if self.head is None:
            return None
        data = self.head.data
        if self.head == self.tail:
            # Если в очереди только 1 элемент
            self.head = None
            self.tail = None
        else:
            # Иначе удаляем первый элемент и перемещаем указатель на следующий элемент
            self.head = self.head.next_node
        return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        """Магический метод __str__ для получения строкового представления очереди"""
        current_node = self.head
        queue_str = ""
        while current_node:
            queue_str += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return queue_str.strip()
