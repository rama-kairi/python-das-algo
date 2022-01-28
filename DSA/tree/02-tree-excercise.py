class GlobalTree:
    def __init__(self, data) -> None:
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child) -> None:
        child.parent = self
        self.children.append(child)

    def get_level(self) -> int:
        label = 0
        while self.parent:
            label += 1
            self = self.parent
        return label

    def print_tree(self, level):
            if self.get_level() > level:
                return
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.print_tree(level)


if __name__ == '__main__':
    root = GlobalTree("Global")

    india = GlobalTree("India")

    gujarat = GlobalTree("Gujarat")
    gujarat.add_child(GlobalTree("Ahmedabad"))
    gujarat.add_child(GlobalTree("Baroda"))

    karnataka = GlobalTree("Karnataka")
    karnataka.add_child(GlobalTree("Bangluru"))
    karnataka.add_child(GlobalTree("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = GlobalTree("USA")

    nj = GlobalTree("New Jersey")
    nj.add_child(GlobalTree("Princeton"))
    nj.add_child(GlobalTree("Trenton"))

    california = GlobalTree("California")
    california.add_child(GlobalTree("San Francisco"))
    california.add_child(GlobalTree("Mountain View"))
    california.add_child(GlobalTree("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    root.print_tree(3)
