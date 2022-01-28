# Implement a stack using a deque
from collections import deque

# Last in, first out (LIFO) - Data structure that follows the principle of
# "last in, first out" (LIFO)
# The last item added to the stack is the first item to be removed


class Stack:
    def __init__(self):
        self.deque = deque()

    def push(self, val):
        self.deque.append(val)

    def pop(self):
        return self.deque.pop()

    def peek(self):
        return self.deque[-1]

    def is_empty(self):
        return len(self.deque) == 0

    def __len__(self):
        return len(self.deque)

    def __str__(self):
        return str(self.deque)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()

    print(stack)
    print(stack.peek())
    print(stack.is_empty())
    print(stack.__str__())
