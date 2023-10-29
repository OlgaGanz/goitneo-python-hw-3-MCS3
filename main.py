from address_book import AddressBook, Record

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    book = AddressBook()

    try:
        book.load("address_book.pkl")
    except FileNotFoundError:
        pass

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            book.save("address_book.pkl")
            print("Good bye!")
            break
        elif command == "add":
            if len(args) == 2:
                name, phone = args
                book.add_record(Record(name, phone))
                print(f"Added {name} with phone {phone}.")
            else:
                print("Invalid arguments. Expected: add [name] [phone]")
        elif command == "change":
            if len(args) == 2:
                name, new_phone = args
                book.change_phone(name, new_phone)
                print(f"Phone for {name} changed to {new_phone}.")
            else:
                print("Invalid arguments. Expected: change [name] [new phone]")
        elif command == "phone":
            if args:
                name = args[0]
                phone = book.get_phone(name)
                if phone:
                    print(phone)
                else:
                    print(f"No phone number found for {name}.")
            else:
                print("Invalid arguments. Expected: phone [name]")
        elif command == "all":
            for record in book.book:
                print(record)
        elif command == "add-birthday":
            if len(args) == 2:
                name, birthday = args
                record = book.get_record(name)
                if record:
                    record.add_birthday(birthday)
                    print(f"Birthday for {name} set to {birthday}.")
                else:
                    print(f"No record found for {name}.")
            else:
                print("Invalid arguments. Expected: add-birthday [name] [birthday]")
        elif command == "show-birthday":
            if args:
                name = args[0]
                birthday = book.get_birthday(name)
                if birthday:
                    print(birthday)
                else:
                    print
