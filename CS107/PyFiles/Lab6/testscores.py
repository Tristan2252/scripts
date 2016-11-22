"""
    had a hard time figuring out how to program this project.
    some of the issues i had:

     *  getting the bins to show correctly
     *  the scaling of sat and act scores when i had to put both in the same graph
     *  i couldn't figure out how to use .bar() properly

"""


import matplotlib.pyplot as plt


def avg_act(lst):
    """
    for every line in the list the function splits the line
    and finds the act score by getting the index 1 of the
    line and then converts it to an int and adds it to the
    list of scores
    :param lst: []  # lines of the file
    :return: []  # list of the act scores
    """
    scores = []
    for line in lst:
        numbers = line.split()
        for num, i in enumerate(numbers):
            if num == 2:
                score = float(i)
                scores.append(score)
    return scores


def get_sat(lst):
    """
    gets the sat scores of each line and adds them to a list
    :param lst:
    :return:
    """
    scores = []
    for line in lst:
        contents = line.split()
        temp_scores = []
        for num, i in enumerate(contents):
            if num >= 4:
                score = int(i)
                temp_scores.append(score)
        scores.append(temp_scores)
    return scores


def sat_convert(scors):
    """
    takes in all sat scores and gets the average by adding each
    sat score per line and dividing by 3 because there are 3 lines
    :param scors: [] # list of lists of act scores
    :return: [] list of average act score
    """
    avg_lst = []
    for i in scors:
        average = 0
        for num in i:
            average += num
        avg_lst.append(average / 3)
    return avg_lst


def act_hist(scores):
    """
    creates a histogram for the ACT scores. A histogram of
    average ACT scores with bins of size 1 between a score
    of 18 and 24.
    :param scores: []  # list of ACT scores
    :return:
    """
    print()
    plt.hist(scores, bins=51)
    plt.show()


def main():
    """
    had a hard time figuring out how to program this project.
    some of the issues i had:

     *  getting the bins to show correctly
     *  the scaling of sat and act scores when i had to put both in the same graph
     *  i couldn't figure out how to use .bar() properly

    :return:
    """
    with open("astsat.txt", "r") as f:
        lines = f.readlines()

# ------------------ ACT hist ---------------------
    print(avg_act(lines))
    act = avg_act(lines)
    act_hist(act)
# -------------------------------------------------
    sat_scores = get_sat(lines)
    sat = sat_convert(sat_scores)
    print()
    print(sat)
    act_list = []
    sat_list = []
    # convert = 0
    for i in act:
        convert = round((i / 36) * 100)
        act_list.append(convert)
    for i in sat:
        convert = round((i / 800) * 100)
        sat_list.append(convert)
    print()
    print(act_list)
    print()
    print(sat_list)
    plt.hist(act_list, alpha=0.5)
    plt.hist(sat_list, alpha=0.5)
    plt.show()

if __name__ == '__main__':
    main()