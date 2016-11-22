import functools


def prompt_fractions():
    """
    prompts the user to enter a fraction and tests if the input is valid
    :return: []  # list of inputted fractions
    """
    fraction_list = []
    while True:
        fraction = input("Enter a fraction: ")
        try:
            if fraction == "stop":
                break
            if "/" not in fraction:
                print("Need to use '/' to represent a fraction")
            else:
                frac = tuple(map(int, fraction.split("/")))
                fraction_list.append(frac)
        except ValueError:
            print("\nNot a Fraction\n")
            pass

    return fraction_list


def min_frac(x, y):
    """
    finds the smallest fraction between two fractions, X and Y
    :param x: () # fraction one
    :param y: () # fraction two
    :return: () # smaller fraction
    """
    if (x[0] / x[1]) >= (y[0] / y[1]):
        return y
    if (x[0] / x[1]) <= (y[0] / y[1]):
        return x


def reduce_frac(frac):
    """
    function that takes in a tuple representing numerator and denominator of a fraction and
    reduces the fraction to its simplest from and returns the new fraction.
    source: http://www.dreamincode.net/forums/topic/193784-function-to-reduce-basic-fractions/
    :param frac:
    :return:
    """
    if frac[1] == 0:
        return "Division by 0 - result undefined"

    smaller = min(frac[0], frac[1])

    for i in range(smaller, 1, -1):
        if frac[0] % i == 0 and frac[1] % i == 0:
            answer = "{}/{}".format(frac[0] // i, frac[1] // i)
            return answer
    else:
        return frac[0], frac[1]


def reduced(frac):
    """
    function that takes in a tuple representing numerator and denominator of a fraction and
    reduces the fraction to its simplest from and returns the new fraction.
    source: http://www.dreamincode.net/forums/topic/193784-function-to-reduce-basic-fractions/
    :param frac:
    :return:
    """
    if frac[1] == 0:
        return "Division by 0 - result undefined"

    smaller = min(frac[0], frac[1])

    for i in range(smaller, 1, -1):
        if frac[0] % i == 0 and frac[1] % i == 0:
            break
    else:
        return frac[0], frac[1]


def sum_frac(frac1, frac2):
    """
    finds the sum of two fractions
    :param frac1: () # fraction 1
    :param frac2: () # fraction 2
    :return: () # sum of both fractions
    """
    num1, denom1 = frac1
    num2, denom2 = frac2
    numerator = (num1 * denom2) + (num2 * denom1)
    denominator = (denom1 * denom2)
    fracsum = (numerator, denominator)
    return fracsum


def sort_frac(fractions):
    """
    sorts fractions by converting them into decimals and attaching the decimal
    to the fraction in a list t and then sorting by the 2 element using lambda as
    a key for the sorted function
    :param fractions: [] # list of fractions
    :return: [] # sorted list
    """
    fraction_lst = []
    new_lst = []
    for frac in fractions:
        decimal = frac[0] / frac[1]
        answer = (frac[0], frac[1]), decimal
        fraction_lst.append(answer)

    sorted_lst = sorted(fraction_lst, key=lambda x: x[1])
    for fraction, i in sorted_lst:
        new_lst.append(fraction)

    return new_lst


def main():
    list_fractions = prompt_fractions()

    format_frac = lambda frac: "{}/{}".format(frac[0], frac[1])

    smallest = functools.reduce(min_frac, list_fractions)
    print("\nSmallest fraction:", format_frac(smallest))

    sumfrac = functools.reduce(sum_frac, list_fractions)
    print("Sum of fractions:", sumfrac)

    reducedfrac = list(map(reduce_frac, list_fractions))
    print("Reduced fractions:", reducedfrac)

    reduce_frac2 = list(filter(reduced, list_fractions))
    print("Simplest Fractions: ", reduce_frac2)

    fracsorted = sort_frac(list_fractions)
    print("Sorted fractions:", fracsorted)


if __name__ == "__main__":
    main()