"""Implement a queue using a list in Python. 
Include the necessary methods such as enqueue, dequeue, and isEmpty."""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0


if'__name__'=='__main__':
    queue = Queue()
    print(queue.isEmpty())  # True

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.isEmpty())  # False

    print(queue.dequeue())  # 10
    print(queue.dequeue())  # 20
    print(queue.dequeue())  # 30
    print(queue.isEmpty())  # True
