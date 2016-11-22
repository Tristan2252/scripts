import book
import random


def menu():
    """
    print menu for user to see available commands to run
    :return: str # menu presented to user
    """
    menu_lst = ("\n\ttype:"
                "\n\t-------------------------------------------------------------------------"
                "\n\t* 'save' to save your contacts \t       * 'add' to add contacts"
                "\n\t* 'edit' to edit a contact     \t       * 'remove' to remove a contact"
                "\n\t* 'view' to view a list of contacts    * 'exit' to close the program"
                "\n\t* 'menu' to review the menu    \t       * 'about' to view developer info"
                "\n\t* 'import' it import contacts from .csv file"
                "\n\t-------------------------------------------------------------------------")

    return print(menu_lst)


def run_cmd():
    """
    tests for command from user and matches command with
    functions needed to execute desired command.
    :return: None
    """
    cmds = ("save", "add", "edit", "remove", "view",
            "exit", "menu", "about", "import")
    while True:
        cmd = input("\n\tWhat would you like to do? ")
        if cmd in cmds:

            if cmd == "save":
                add = book.get_book()
                view_all()
                book.save_contacts(add)
                print("\n\tContacts saved....")

            if cmd == "add":
                contact = book.get_info()
                book.add_info(contact)

            if cmd == "edit":
                book.edit()

            if cmd == "remove":
                book.remove()
                view_all()

            if cmd == "view":
                view()

            if cmd == "exit":
                book.save_contacts(book.get_book())
                print(goodbye())
                break

            if cmd == "menu":
                menu()

            if cmd == "about":
                about()
                readme = input("\n Would you like to view README for more info (y/N) ")
                if readme == "y":
                    book.readme()

            if cmd == "import":
                book.import_file()

        else:
            print("\n Option is not available...")


def view():
    """
    asks user what contact they would like to view and prints
    out the contact into of the desired contact.
    :return: None
    """
    while True:
        contact_name = input("\n > Enter the name of a contact you want to view,\n"
                             "    all to vew all contacts, or back to main menu: ")
        try:
            print()
            if contact_name == "all":
                view_all()
            elif contact_name == "back":
                break
            elif contact_name:
                contents = book.get_book()
                for i, value in enumerate(contents[contact_name]):
                    if i == 0:
                        number = "({}) {}-{}".format(value[:3], value[3:6], value[6:])
                    if i == 1:
                        company = value
                    if i == 2:
                        email = value
                    if i == 3:
                        notes = value
                print("\t-------------------------------------------------------------------------"
                      "\n\t* {}, {}, {}, {}, {},\n"
                      "\t-------------------------------------------------------------------------"
                      "".format(contact_name, number, company, email, notes))

        except KeyError:
            print("\n *** Name not found *** ")


def view_all():
    """
    similar to view() but instead prints all contacts not just one
    :return: None
    """
    contents = book.get_book()
    print("\n\tContacts list:    Number of contacts found: {}\n"
          "\t-------------------------------------------------------------------------"
          "".format(len(book.get_book())))
    for key, value in contents.items():
        split_num = value[0].split()
        for i in split_num:
            number = "({}) {}-{}".format(i[:3], i[3:6], i[6:])
            print("\t* {} {} {}, {}, {}".format(key, number, value[1], value[2], value[3]))
    print("\t-------------------------------------------------------------------------")


def not_found():
    """
    if default file is not found this function is ran to ask user
    if they would like to input a file or create new default file.
    :return: None
    """
    answer = input("\tWould you like to import an existing file (y/n) ")
    if answer == "y":
        book.import_file()
        print("\n\t*** "
              "Your contacts have been imported to contacts.csv"
              " ***")
        menu()
        run_cmd()
    elif answer == "n":
        print("\tCreating new default contact file....")
        book.save_contacts(book.get_book())
        main()


def about():
    """
    prints developer info for user
    :return: None
    """
    print("\n"
          "\t\t >>> PERSONAL CONTACTS PROGRAM                 <<<\n"
          "\t\t >>> Developed By: Tristan Vigil for CSE-107   <<<\n"
          "\t\t >>> Date created: March 12th 2015             <<<")


def welcome():
    """
    chooses a random welcome message
    :return: str  # displayed welcome
    """
    welcome_msg = random.choice([" Welcome awesome user",
                                 " Nice to see you back!!",
                                 " Good to see you again",
                                 " Welcome!! :)"])
    return welcome_msg


def goodbye():
    """
    chooses a random goodbye message
    :return: str # displayed goodbye
    """
    goodbye_msg = random.choice(["\n Goodbye :)\n",
                                 "\n So sad to see you go\n",
                                 "\n See you next time... :)\n",
                                 "\n Later!!!\n"])
    return goodbye_msg


def main():
    print("\n\n\t\t\t=== PERSONAL PHONE BOOK PROGRAM ===")
    default_file = "contacts.csv"
    book.check_file(default_file)
    if not book.check_file(default_file):
        print("\n\t *** Default File Not Found ***")
        not_found()
    else:
        book.load_book("contacts.csv")
        print("\n Saved Contacts Loaded....\n")
        print(welcome())
        menu()
        run_cmd()



if __name__ == '__main__':
    main()