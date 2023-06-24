"""Implement a stack using a list in Python. 
Include the necessary methods such as push, pop, and isEmpty."""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0


if '__name__'=='__main__':
    stack = Stack()
    print(stack.isEmpty())  # True

    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.isEmpty())  # False

    print(stack.pop())  # 30
    print(stack.pop())  # 20
    print(stack.pop())  # 10
    print(stack.isEmpty())  # True
