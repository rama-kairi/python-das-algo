class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_first(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_last(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_first(data)
            return
        current = self.head
        for _ in range(position - 1):
            current = current.next
        node = Node(data, current.next)
        current.next = node

    def insert_values(self, data_list: list):
        self.head = None
        for i in data_list:
            self.insert_at_last(i)

    def delete_at_first(self):
        if self.head is None:
            print("Linked List is empty")
            return
        self.head = self.head.next

    def delete_at_last(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if position == 0:
            self.delete_at_first()
            return
        current = self.head
        for _ in range(position - 1):
            current = current.next
        current.next = current.next.next

    def linkedlist_length(self):
        if self.head is None:
            return 0
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return print(count)

    def insert_after_value(self, data, value):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current.data != value:
            current = current.next
        node = Node(data, current.next)
        current.next = node

    def delete_after_value(self, value):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current.data != value:
            current = current.next
        current.next = current.next.next

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        ll_str = ""
        while current is not None:
            ll_str += str(current.data) + "->"
            current = current.next
        print(ll_str)


if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.insert_values([1, 2, 3, 4, 5, 6, 7, 8, 9])
    linkedlist.linkedlist_length()

    linkedlist.print()

    linkedlist.delete_after_value(5)
    linkedlist.print()

    linkedlist.insert_after_value(10, 5)
    linkedlist.print()
