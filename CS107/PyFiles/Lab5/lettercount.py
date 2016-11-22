

def cnt_letters(letter_list):
    """
    function that receives a list of sorted letters and counts how many
    times a letter occurs in the list
    :param letter_list:
    :return: letters and their counted numbers
    """
    temp = None
    letter_cnt = {}
    for i in letter_list:
        if i == temp:
            pass
        else:
            letter_cnt[i] = letter_list.count(i)
            print("'{}' {}".format(i, letter_cnt[i]))
            temp = i
    """
    Source for '.count' function:
    http://stackoverflow.com/questions/1155617/count-occurrence-of-a-character-in-a-string
    """


def sort_list(lst):
    """
    function that sorts a list and returns the list sorted
    :param lst: []
    :return: sorted version list
    """
    sort_lst = sorted(lst)
    return sort_lst


def main():
    # string1 = "this is a test"
    string1 = input("\nEnter a string: ")
    sort_str = sort_list(string1)
    cnt_letters(sort_str)

if __name__ == '__main__':
    main()