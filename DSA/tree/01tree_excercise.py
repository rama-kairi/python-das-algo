class EmployeeTree:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child) -> None:
        child.parent = self
        self.children.append(child)

    def get_label(self) -> int:
        label = 0
        while self.parent:
            label += 1
            self = self.parent
        return label

    def print_tree(self, tree_type) -> None:
        spaces = ' ' * self.get_label() * 3
        prefix = spaces + '|__' if self.parent else ''
        if tree_type == "name":
            print(prefix + self.data['name'])
        elif tree_type == "designation":
            print(prefix + self.data.get('designation', 'No designation'))
        elif tree_type == "both":
            print(prefix + self.data['name'] + " " + f"({self.data.get('designation', 'No designation')})")
        if self.children:
            for child in self.children:
                child.print_tree(tree_type)


if __name__ == '__main__':
    nilupul = EmployeeTree({'name': 'Nilupul', 'designation': 'CEO'})

    chinmay = EmployeeTree({'name': 'Chinmay', 'designation': 'Manager'})

    nilupul.add_child(chinmay)

    viswa = EmployeeTree({'name': 'Viswa', 'designation': 'Infrastructure Head'})

    chinmay.add_child(viswa)
    daval = EmployeeTree({'name': 'Daval', 'designation': 'Cloud Manager'})
    abhjit = EmployeeTree({'name': 'Abhjit', 'designation': 'App Manager'})
    viswa.add_child(daval)
    viswa.add_child(abhjit)
    amir = EmployeeTree({'name': 'Amir', 'designation': 'Application head'})
    chinmay.add_child(amir)

    gels = EmployeeTree({'name': 'Gels', 'designation': 'HR Head'})
    nilupul.add_child(gels)

    peter = EmployeeTree({'name': 'peter', 'designation': 'Recruitment Manager'})
    waqas = EmployeeTree({'name': 'Waqas', 'designation': 'Policy Manager'})

    gels.add_child(peter)
    gels.add_child(waqas)


    nilupul.print_tree("both")
