class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item, self.head)
        self.head = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self.head.value
        self.head = self.head.next
        return value


if __name__ == "__main__":
    stack = Stack()
    for item in ("Hello,", "world!"):
        stack.push(item)
    while not stack.is_empty():
        print(stack.pop())