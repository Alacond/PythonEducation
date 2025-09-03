class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.head = None  # первый элемент
        self.tail = None  # последний элемент

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty queue")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value


if __name__ == "__main__":
    queue = Queue()
    for item in ("Hello,", "world!"):
        queue.push(item)
    while not queue.is_empty():
        print(queue.pop())