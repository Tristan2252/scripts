def find_operation(x, y, operation):
    """
    function that take in 2 numbers x and y as well as string representing
    the mathematical operation that is to be preformed with the 2 numbers.
    if statements test for the correct operation and if true the operation
    is preformed.
    :param x: int
    :param y: int
    :param operation: str
    :return: int solution
    """
    if operation == "+":
        return x + y
    if operation == "-":
        return x - y
    if operation == "*":
        return x * y
    if operation == "/":
        return x / y


def split_str(string):
    """
    iterates through each character in the string and adds it
    to a new list
    :param string: str
    :return: str_list: []
    """
    splitted_str = string.split()
    return splitted_str


def build_stack(splitted_str):
    """
    creates a stack to add the numbers in the RPN code to and
    then iterates through the list. if an operator is found, the
    last two numbers of the operator are poped and the operation
    is performed then the answer is added to the stack
    :param splitted_str: []
    :return: float of stack index 0
    """
    operators = ("/", "*", "+", "-")
    stack = []
    for i in splitted_str:
        if i in operators:
            last = float(stack.pop())
            first = float(stack.pop())
            answer = find_operation(first, last, i)
            stack.append(answer)
            print(answer)
        else:
            stack.append(i)
            print(stack)

    return stack[0]


def main():
    code = input("\nEnter RPN Expression: ")
    # tst = "5 1 2 / 4 * + 3 -"
    ordered_str = split_str(code)
    answer = build_stack(ordered_str)
    print("\n{} is equal to: {}".format(code, answer))


if __name__ == '__main__':
    main()