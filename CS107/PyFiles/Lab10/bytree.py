class Node():
 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
    def append(self, value):
        if value < self.value:
            # left side:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.append(value)
        else: # larger or equal
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.append(value)
 
    def ordered_list(self):
        if self.left is None and self.right is None:
            return [self.value]
        if self.left is not None and self.right is None:
            return self.left.ordered_list() + [self.value]
        if self.left is None and self.right is not None:
            return [self.value] + self.right.ordered_list()
        if self.left is not None and self.right is not None:
            return self.left.ordered_list() + [self.value] + self.right.ordered_list()
 
class BinarySearchTree():
 
    def __init__(self):
        self.root = None
 
    def append(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.append(value)
 
    def ordered_list(self):
        if self.root is None:
            return []
        else:
            return self.root.ordered_list()
 
    def rebalance(self):
        ordered_list = self.ordered_list()
        middle = len(ordered_list) / 2
        self.root = Node(ordered_list[middle])
        self.root.left = self.build_tree(ordered_list[:middle])
        self.root.right = self.build_tree(ordered_list[middle+1:])
 
    def build_tree(self, ordered_list):
        if len(ordered_list) == 0:
            return None
        elif len(ordered_list) == 1:
            return Node(ordered_list[0])
        elif len(ordered_list) == 2:
            node = Node(ordered_list[0])
            node.append(ordered_list[1])
            return node
 
        middle = len(ordered_list) / 2
        node =  Node(ordered_list[middle])
        node.left = self.build_tree(ordered_list[:middle])
        node.right = self.build_tree(ordered_list[middle+1:])
        return node
 
if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.append(4)
    tree.append(3)
    tree.append(9)
    tree.append(1)
    tree.append(9)
    tree.append(10)
    print tree.ordered_list()
    tree.rebalance()
    print tree.ordered_list()
