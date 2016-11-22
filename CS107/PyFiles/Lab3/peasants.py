
def multiply(x, y,):
    answer = 0
    while y >= 1:

        if (y % 2) != 0:
            answer = answer + x
        # if (y % 2) < 1:
        #  break
        print("----------------------")
        print("{} | {}".format(x, y))
        x *= 2
        y //= 2
        print("----------------------")
        print("Answer is currently {}".format(answer))
    return answer


def expo(x, y):
    if y == 1:
        return x
    elif y % 2 == 0:
        answer = expo(x * x, y / 2)
        return answer
    else:
        answer = x * expo(x * x, (y-1) / 2)
        return answer


def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number to multiply {} by and raze {} to the power of ".format(x, x)))
    # x = 7
    # y = 5
    print()
    print("Russian peasant multiplication non-recursive method")
    print("{} * {} =".format(x, y))
    print()
    print("Answer = {}".format(multiply(x, y)))
    print()
    print("Exponentiation by squaring recursive method")
    print("Answer = {}".format(expo(x, y)))


if __name__ == "__main__":
    main()