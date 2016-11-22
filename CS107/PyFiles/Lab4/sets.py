# checks for overlap between two lists by iterating through one list and checking if the index value is in list 2
def overlap(list1, list2):
    final_list = []
    for i in list1:
        if i in list2:
            final_list.append(i)

    return final_list

# joins the two lists by checking for duplicates and then adding them to a final list
def join(list1, list2):
    final_list = []
    for i in list1:
        if i in list2:
            final_list.append(i)
        else:
            final_list.append(i)
    for i in list2:
        if i not in final_list:
            final_list.append(i)

    return final_list

# function used to make a list from the user input. if user inputs stop function is exited
def make_lst(lst):
    ext_loop = False
    while not ext_loop:
        number = input("Enter a number >>> ")
        if number == "stop":
            ext_loop = True
        else:
            lst.append(number)
    return lst


def main():
    # listA = [1, 2, 3, 4, 5]
    # listB = [2, 5, 1, 10]
    listA = []
    listB = []

    print("\nList 1")
    make_lst(listA)
    print("\nList 2")
    make_lst(listB)

    print("\nOverlap is: {}".format(overlap(listA, listB)))
    print("Join is: {}".format(join(listA, listB)))

if __name__ == '__main__':
    main()