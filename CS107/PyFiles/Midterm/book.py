
import csv

phone_book = {}  # dictionary that all contacts are added to


def get_info():
    """
    gets the info for a new contact from the user such as name
    number company etc... and then adds the items to a contact
    info list to return
    :return: []  # list of the contact info
    """
    contact_info = []
    print()
    name = add_name()
    number = add_number()
    company = add_company()
    email = add_email()
    notes = add_notes()
    contact_info.extend((name, number, company, email, notes))
    return contact_info


def add_name():
    """
    asks the user for a name to title the contact they are adding
    tests for no input and prompts the user to enter a valid name
    :return: str  # the name of the contact
    """
    while True:
        name = input(" > Name: ")
        if name == "":  # no name is not accepted
            print("  > Enter a name for your contact <")
            continue
        else:
            return name


def add_number():
    """
    asks the user to enter a number for the contact they are creating.
    number includes area code so if the number is not = to 10 digits
    the user is asked to renter a valid number.
    :return: int  # contact phone number
    """
    while True:
        num = input(" > Number: ")
        try:
            if len(num) == 10:
                number = int(num)
                return number
            else:
                print("  > Not a valid phone number.\n   Area code included with no dashes <")
        except ValueError:
            print("  > Input must contain numbers only.\n   Area code included with no dashes <")


def add_company():
    """
    asks the user to add a company, any input is valid even no input.
    :return: str  # the name of the company for the contact
    """
    company = input(" > Company: ")
    return company


def add_email():
    """
    asks the user for an email to add to the contact, no email is
    accepted.if the user inputs a string not containing @ they
    are presented with an error.
    :return: str  # string identifying the email of the contact
    """
    while True:  # checks for "@" in inputted string
        email = input(" > Email: ")
        if "@" in email:
            return email
        if email == "":  # no email is accepted
            return email
        else:
            print("  > Not a valid email <")


def add_notes():
    """
    user asked for notes to add to the contact, any input is accepted
    :return: str  # notes to add to the contact
    """
    notes = input(" > Contact Notes: ")
    return notes


def add_info(contact_list):
    """
    adds a new contact to the phone book and is stored in mem in
    the phone book dictionary. save_contacts(phone_book) saves
    the newly added contact to the default file and the new file
    is reloaded to the program with load_book().
    :return: None
    """
    phone_book[contact_list[0]] = [contact_list[1],
                                   contact_list[2],
                                   contact_list[3],
                                   contact_list[4]]
    save_contacts(phone_book)
    load_book("contacts.csv")


def remove():
    """
    removes selected contact from the phone book dictionary by popping
    if the user inputs none the function is exited.
    :return: None
    """
    name = input("\n > Who would you like to remove from contacts"
                 "\n   type none to remove no contacts: ")
    while True:
        try:
            phone_book.pop(name)
            print("   {} removed".format(name))
            break
        except KeyError:
            if name == "none":
                break
            print("\n  {} not found in contacts...\n".format(name))
            name = input(" > Try a different name: ")


def edit():
    """
    tests for commands from the user on what to change in the contact
    if the user is changing something the content is added to temp
    list and the contact being changed is removed from the phone book
    a new contact is created and added to phone book in the place of
    the old contact
    :return:
    """
    while True:
        name = input("\n > Enter the name of the contact you would like to change"
                     "\n   or type 'back' to go to main menu: ")
        try:
            temp_list = phone_book[name]
            print("\n\t ------------------------"
                  "\n\t * name     \t* number "
                  "\n\t * company  \t* email  "
                  "\n\t * notes    \t         "
                  "\n\t ------------------------ \n")
            cmd = input(" > What would you like to change: ")
            cmds = ("name", "company", "number", "email", "notes", "back")
            if cmd in cmds:
                if cmd == "name":
                    del phone_book[name]
                    new_name = add_name()
                    phone_book[new_name] = temp_list
                    print("\n   Name changed to {}".format(new_name))
                if cmd == "number":
                    del phone_book[name]
                    new_number = add_number()
                    temp_list[0] = new_number
                    phone_book[name] = temp_list
                    print("\n   Number changed to {}".format(new_number))
                if cmd == "company":
                    del phone_book[name]
                    new_string = add_company()
                    temp_list[1] = new_string
                    phone_book[name] = temp_list
                    print("\n   Company changed to {}".format(new_string))
                if cmd == "email":
                    del phone_book[name]
                    new_string = add_email()
                    temp_list[2] = new_string
                    phone_book[name] = temp_list
                    print("\n   Email changed to {}".format(new_string))
                if cmd == "notes":
                    del phone_book[name]
                    new_string = add_notes()
                    temp_list[3] = new_string
                    phone_book[name] = temp_list
                    print("\n   Notes changed to {}".format(new_string))
            else:
                print("\n Option not available...")
        except KeyError:
            if name == "back":
                break
            print("\n Name doesn't exit in contacts...")


def save_contacts(contacts_lst):
    """
    saves the list of contacts made while the program is running into a
    csv file named contacts.
    :param contacts_lst: {}  # dictionary of contacts
    :return: None
    """
    with open("contacts.csv", "w") as csvfile:
        w = csv.writer(csvfile)
        for i in contacts_lst:
            temp_lst = [i]
            for a in contacts_lst[i]:
                temp_lst.append(a)
            w.writerow(temp_lst[0:])


def get_book():
    """:return: {}  # returns phone book"""
    return phone_book


def get_contact(name):
    """
    take in a string name used as a key to find the contents of
    the contact
    :param name: str # name of the contact the user wants to see
    :return: [] # list of the contents in the contact
    """
    return phone_book[name]


def load_book(book_name):
    """
    opens the csv file containing the contacts and loads them into
    a dictionary to be used throughout the program. The first item
    in every row is the key of the dictionary and the remaining
    items are the values. Each line is a new contact in the file.
    :param book_name: str   # name of the file to open
    :return: {}  # converted file
    """
    with open(book_name, "r") as csvfile:
        book = csv.reader(csvfile)
        for i, row in enumerate(book):
                phone_book[row[0]] = row[1:]
    return phone_book


def check_file(file_name):
    """
    checks if the specified file can be opened via try and except,
    function returns false if file is not found ans true if it is.
    :param file_name: str # name of the file the user wants to check
    :return: bool # if able to open True and if not False
    """
    try:
        with open(file_name, "r"):
            return True
    except FileNotFoundError:
        return False


def import_file():
    """
    function asks the user for the name of the file they would like to
    import to the program. function checks if the file exists, if so
    the new book is leaded to program dictionary if not the user is
    presented with an error
    :return: None
    """
    while True:
        file_name = input("\n > Enter the name of the file you would"
                          "like to import (include .csv extension): ")
        try:
            load_book(file_name)
            break
        except FileNotFoundError:
            print("\n   File not found... ")


def make_default():
    """
    function creates a default file named 'contacts.csv' for the program
    to use to store contacts to. sample line is added to the file.
    :return:
    """
    with open("contacts.csv", "w") as df_file:
        w = csv.writer(df_file)
        w.writerow("-,-------,-,-,-")
        print("\tcontacts.csv Successfully Created.... ")


def readme():
    found = check_file("README.txt")
    print("\n\n")
    if found:
        with open("README.txt") as fl:
            for line in fl:
                print(line, end="")
    else:
        print("\n Sorry for the inconvenience but the README file is not found")


def main():
    input("\n\tWARNING RUNNING PROGRAM MAY CAUSE DAMAGE TO SAVED CONTACTS OR NOT WORK\n"
          "\nType ENTER to continue: ")
    add_name()
    add_number()
    add_company()
    add_email()
    add_notes()
    print("running add_info()")
    add_info(["name", "5050000000", "company", "eamil@mail.com", "notes"])
    print("\tDoes file exit:".format(check_file("contacts.csv")))
    edit()
    get_book()
    # get_contact("Name")
    import_file()
    # load_book("contacts.csv")
    # make_default()
    remove()
    save_contacts(phone_book)



if __name__ == '__main__':
    main()