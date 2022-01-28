import random


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == data:
            return
        elif data < self.data:
            if self.left is None:
                self.left = BinarySearchTreeNode(data)
            else:
                self.left.insert(data)
        elif self.right is None:
            self.right = BinarySearchTreeNode(data)
        else:
            self.right.insert(data)

    # Search for a value in the tree
    def search(self, data):
        if self.data == data:
            return True
        elif data < self.data:
            return (
                False if self.left is None else self.left.search(data)
            )
        else:
            return (
                False if self.right is None else self.right.search(data)
            )

    # in-order traversal
    def in_order_traversal(self):
        elements = []

        # Visit the left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit the root
        elements.append(self.data)

        # Visit the right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # pre-order traversal
    def pre_order_traversal(self):
        elements = [self.data]

        # Visit the left subtree
        if self.left:
            elements += self.left.pre_order_traversal()

        # Visit the right subtree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    # post-order traversal
    def post_order_traversal(self):
        elements = []

        # Visit the left subtree
        if self.left:
            elements += self.left.post_order_traversal()

        # Visit the right subtree
        if self.right:
            elements += self.right.post_order_traversal()

        # Visit the root
        elements.append(self.data)

        return elements

    # Find the minimum value in the tree
    def find_min(self):
        return self.data if self.left is None else self.left.find_min()

    # Find the maximum value in the tree
    def find_max(self):
        return (
            self.data if self.right is None else self.right.find_max()
        )

    # Find the maximum depth of the tree
    def max_depth(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.max_depth() + 1
        elif self.right is None:
            return self.left.max_depth() + 1
        else:
            return (
                max(self.left.max_depth(), self.right.max_depth()) + 1
            )

    # Delete a node from the tree
    def delete(self, data):
        if self.data == data:
            # Case 1: No children
            if self.left is None and self.right is None:
                return None

            # Case 2: One child
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # Case 3: Two children
            temp = self.right.find_min()
            self.data = temp
            self.right.delete(temp)

        elif data < self.data:
            self.left = self.left.delete(data)
        else:
            self.right = self.right.delete(data)

        return self


# helper method to build tree
def build_tree(elements: list):
    root = BinarySearchTreeNode(elements[0])
    for element in elements[1:]:
        root.insert(element)
    return root


# main method
def main():
    # elements = [5, 3, 7, 2, 4, 6, 8, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    # root = build_tree(elements)
    # print(root.in_order_traversal())
    # print(root.search(55))

    countries = [
        "Canada",
        "China",
        "France",
        "Germany",
        "India",
        "Italy",
        "Japan",
        "Russia",
        "United States",
    ]
    root = build_tree(countries)
    print(root.post_order_traversal())
    print(root.search("Canada"))
    print(root.search("United States"))
    print(root.find_min())
    print(root.find_max())
    print(root.max_depth())
    print(root.delete("United States"))
    print(root.post_order_traversal())

    # randon_thousand_numbers = [random.randint(0, 10000) for _ in range(10000)]
    # root = build_tree(randon_thousand_numbers)
    # print(root.pre_order_traversal())
    # print(root.search(55))


if __name__ == "__main__":
    main()
