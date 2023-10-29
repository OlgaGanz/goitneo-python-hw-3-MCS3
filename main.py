from address_book import AddressBook, Record

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add" and len(args) == 2:
            record = Record(args[0], args[1])
            book.add_record(record)
            print("Contact added.")

        elif command == "change" and len(args) == 2:
            updated = book.change_phone(args[0], args[1])
            if updated:
                print("Contact updated.")
            else:
                print(f"No contact named {args[0]} found.")

        elif command == "phone" and len(args) == 1:
            phone = book.find_phone(args[0])
            if phone:
                print(phone)
            else:
                print(f"No contact named {args[0]} found.")

        elif command == "all":
            print(book.show_all_records())

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
