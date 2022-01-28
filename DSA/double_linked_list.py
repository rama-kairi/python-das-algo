# Implement a Double Linked List

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data) -> None:
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data, prev=self.tail)
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data) -> None:
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data, next=self.head)
            self.head.prev = new_node
            self.head = new_node

    def length(self) -> int:
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def insert(self, data, index) -> None:
        if index == 0:
            self.prepend(data)
        elif index == self.length():
            self.append(data)
        else:
            temp = self._updater(index)
            new_node = Node(data, next=temp, prev=temp.prev)
            temp.prev.next = new_node
            temp.prev = new_node

    def remove(self, index) -> None:
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.length() - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            temp = self._updater(index)
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

    def _updater(self, index):
        result = self.head
        i = 0
        while i < index:
            result = result.next
            i += 1
        return result

    def print_list(self) -> None:
        temp = self.head
        dll_str = ""
        while temp:
            dll_str += str(temp.data) + " "
            temp = temp.next

        print(dll_str)


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    dll.insert(4, 2)
    print(dll.length())
    dll.remove(0)
    dll.print_list()
