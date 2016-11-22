
# prints all numbers in the list
def all_num(num_list):
    return "All Numbers {}".format(num_list)

# sum of all the number in a list by going through each index and adding it ot answer
def all_sum(num_lsit):
    answer = 0
    for i in num_lsit:
        answer += i
    return answer

# average of all the numbers in a list by getting the len of the list and calling the all_sum function
# then dividing them
def all_avrg(num_list):
    length = len(num_list)
    num_sum = sum(num_list)
    return num_sum / length

# makes a list of all even numbers in a list by adding numbers whos reader is = 0 when divided by 2
def evn(num_list):
    evn_lst = []
    for i in num_list:
        if i % 2 == 0:
            evn_lst.append(i)
        continue
    return evn_lst


# smae as All_sum except for even numbers
def evn_sum(num_list):
    numbers = evn(num_list)
    answer = 0
    for i in numbers:
        answer += i
    return answer

# smae as All_avg except for even numbers
def evn_avg(num_list):
    length = len(evn(num_list))
    num_sum = evn_sum(num_list)
    return length / num_sum

# makes a list of all odd numbers in a list by adding numbers whos reader is > 0 when divided by 2
def odd(num_list):
    odd_list = []
    for i in num_list:
        if i % 2 != 0:
            odd_list.append(i)
        continue
    return odd_list


# smae as All_sum except for odd numbers
def odd_sum(num_list):
    numbers = odd(num_list)
    answer = 0
    for i in numbers:
        answer += i
    return answer

# smae as All_avg except for even numbers
def odd_avg(num_list):
    length = len(odd(num_list))
    num_sum = odd_sum(num_list)
    return length / num_sum


def main():
    ext_loop = False
    numbers = []
    while not ext_loop:
        option = input("Input a number >>> ")

        if option == "stop":
            ext_loop = True
        else:
            number = int(option)
            numbers.append(number)
    print()
    print(all_num(numbers))
    print("Average of all numbers: {}".format(all_avrg(numbers)))
    print("Sum of all numbers: {}".format(all_sum(numbers)))
    print("Even numbers: {}".format(evn(numbers)))
    print("Average of even numbers: {}".format(evn_avg(numbers)))
    print("Sum of even numbers: {}".format(evn_sum(numbers)))
    print("Odd numbers: {}".format(odd(numbers)))
    print("Average of odd numbers: {}".format(odd_avg(numbers)))
    print("Sum of odd numbers: {}\n".format(odd_sum(numbers)))

if __name__ == "__main__":
    main()