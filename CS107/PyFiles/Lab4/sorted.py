

def main():
    ext_loop = False
    num_list = []
    while not ext_loop:
        number = input("Input a number >>> ")
        if number == "stop":
            ext_loop = True  # sets while boolean to true
        else:
            num = int(number)
            num_list.insert(-1, num)  # inserts the input number in index -1 in the list
            num_list.sort()  # could not figure out how to sort without using .sort()
            print(num_list)  # showing work

    print("\n{}".format(num_list))

if __name__ == '__main__':
    main()