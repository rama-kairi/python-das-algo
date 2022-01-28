# Implement Queue using Stacks (FIFO)

from collections import deque

# https://www.bigocheatsheet.com/


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, val):
        self.queue.appendleft(val)

    def dequeue(self):
        self.queue.pop()

    def peek(self):
        pass

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()

    print(queue)
    print(queue.peek())
    print(queue.is_empty())
    print(queue.__str__())
