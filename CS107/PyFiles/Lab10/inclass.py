class LinkedList(object):
    def __init__(self, value):
        self._value = value
        self._next = None

    def append(self, v):
        if self._next is None:
            self._next = LinkedList(v)
        else:
            self._next.append(LinkedList(v))

    def __str__(self):
        return "Value {}".format(self._value)

    def __iter__(self):
        self.stack = [self._value]
        if self.stack:
            self.stack.append(self._next)
        return self

    def __next__(self):
        if self.stack:
            item = self.stack.pop(0)
            if not isinstance(item, int):
                self.stack = list(item)
                item = self.stack.pop(0)
                return item
        else:
            return StopIteration


def main():
    a = LinkedList(12)
    a.append(99)
    # print(a)
    print(list(a))

    for i in a:
        print(i)

if __name__ == '__main__':
    main()