def get_month():
    """
    test if the numerical month is within 1 to 12 because there is no more
    than 12 months in a year
    """
    valid_cmd = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    while True:
        month = input("\nEnter the month: ")
        
        try:
            month = int(month)
            if month in valid_cmd:
                return month
            else:
                print("\n'{}' is not a month, choose a number between 1 and 12\n".format(month))
        except ValueError:
            print("{} is not a valid month".format(month))


def get_weekday():
    """
    Tests for a valid cmd for the user for weekday
    returns cmd if cmd is correct if not prompts the user again
    """
    valid_cmd = ("SU", "M", "TU", "W", "TH", "F", "SA")
    while True:
        weekday = input('                   -- Weekday format --\n'
                        ' "SU": "Sunday", "M": "Monday", "TU": "Tuesday", "W": "Wednesday"\n'
                        ' "TH": "Thursday", "F": "Friday", "SA": "Saturday" '
                        '\nEnter the Weekday: ')

        if weekday in valid_cmd:
            return weekday
        else:
            print("\n '{}' is not a valid command\n".format(weekday))


def get_day(month):
    """
    gets the numerical value for the day of the week form the user
    and tests if the value is a valid day in the month and returns
    day if true
    """
    days_per_mo = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                   7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    while True:
        day = input("Enter the day: ")

        try:  # checking for input errors
            day = int(day)
        
            if day <= days_per_mo[month]:
                return day
            else:
                print("'{}' is not a valid day in month {}".format(day, month))
        except ValueError:
            print("'{}' is not a valid day in month {}".format(day, month))


def get_year():
    """
    gets the year form the user and checks to see if it is valid
    and then returns the value
    :return: int year
    """
    while True:
        number = input("Enter the Year: ")
        try:
            year = int(number)   
            if year > 1:
                return year
            else:
                print("{} is not a year, enter a number grater than 1".format(year))
        except ValueError:
            print("{} is not a year, enter a number grater than 1".format(number))


def cvt_month(month):
    """
    converts the numerical value of the month into its specified string
    by calling the key of the month in the dictionary
    """
    months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
              7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

    return months[month]


def cvt_weekday(weekday):
    """
    converts the shortened string into its full length string by calling
    the key of the day in the dictionary
    """
    weekdays = {"SU": "Sunday", "M": "Monday", "TU": "Tuesday", "W": "Wednesday",
                "TH": "Thursday", "F": "Friday", "SA": "Saturday"}

    return weekdays[weekday]


def date(month, day, year, weekday):
    """
    takes in month day year and weekday and distributes them to be converted
    and orders them in a readable date
    """
    return "\nDate: {} {} {} {}\n".format(cvt_weekday(weekday), cvt_month(month), day, year)


def main():
    """
    Write a function that takes four arguments – day, month, and year as numbers, and weekday
    as MTWRFSU – and converts this date to a human-readable string. Have the program be
    called with user-specified input
    """
    # wht_month = "1"
    # wht_day = "5"
    # wht_year = "2015"
    # wht_weekday = "TH"

    wht_month = get_month()
    wht_day = get_day(wht_month)
    wht_year = get_year()
    wht_weekday = get_weekday()
    print(date(wht_month, wht_day, wht_year, wht_weekday))


if __name__ == '__main__':
    main()
