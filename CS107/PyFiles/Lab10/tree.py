class Tree(object):

    def __init__(self, value):
        """
        initialises variables
        :param value: int
        :return: None
        """
        self._value = value
        self._left = None
        self._right = None

    def add_item(self, item):
        """
        Create a new Tree object and add it to the tree. The new object
        should be added to the child tree with the smallest height
        If there is a tie, favor the left tree.
        :return: None
        """
        if item < self._value:
            if self._left is None:
                self._left = Tree(item)
        else:
            if self._right is None:
                self._right = Tree(item)

    def __iter__(self):
        """
        allows tree to be used as a for loop
        :return: self
        """
        self.stack = [self._value]
        if self._left:
            self.stack.append(self._left)

        return self

    def __next__(self):
        """
        creates a stack for items of the tree to be added to
        :return: item
        """
        if self.stack:
            item = self.stack.pop(0)

            if not isinstance(item, int):
                self.stack = list(item)
                item = self.stack.pop(0)
            return item
        else:
            raise StopIteration


def main():
    a = Tree(10)
    a.add_item(15)
    a.add_item(7)

    print(list(a))

if __name__ == '__main__':
    main()
