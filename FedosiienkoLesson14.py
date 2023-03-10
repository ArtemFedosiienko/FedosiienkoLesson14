class Tree:
    #Завдання 1
    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    #  Метод додавання нових елементів зі списку
    def add_list(self, lst):
        for id_node in lst:
            self.insert(id_node)


    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    # Метод порівняння
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

    # Вивести дерево у консоль
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()
    #Завдання 2
    #  Метод пошуку мінімального значення
    def min_node(self):
         if self.left is None:
             return self.id_node
         return self.left.min_node()

    #  Метод пошуку максимального значення
    def max_node(self):
         if self.right is None:
             return self.id_node
         return self.right.max_node()
    #Завдання 3
    #  Метод видалення елементів
    def del_node(self, node):
        if self is None:
            return self
        if node < self.id_node:
            self.left = self.left.del_node(node)
            return self
        if node > self.id_node:
            self.right = self.right.del_node(node)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        element = self.right
        while min_larger_node.left:
            element = element.left
        self.id_node = element.id_node
        self.right = self.right.del_node(element.id_node)
        return self

my_tree = Tree(5)
my_tree.add_list([15, 12, 9, 10, 5, 6, 7, 1, 2, 4])
my_tree.print_tree()

print("Min element:", my_tree.min_node())
print("Max element:", my_tree.max_node())

my_tree.del_node(10)
my_tree.print_tree()