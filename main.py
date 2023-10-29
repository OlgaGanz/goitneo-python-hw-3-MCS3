import datetime
from address_book import AddressBook
from record import Record
from phone import Phone
from birthday import Birthday

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

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            if Phone.is_valid(args[1]):
                book.add_record(Record(args[0], args[1]))
                print(f"Added {args[0]} with phone number {args[1]}")
            else:
                print("Invalid phone number. Please enter a 10-digit number.")
        elif command == "change" and len(args) == 2:
            if book.change_phone(args[0], args[1]):
                print(f"Changed phone number for {args[0]} to {args[1]}")
            else:
                print("Error: Contact not found or invalid phone format.")
        elif command == "phone" and len(args) == 1:
            phone = book.get_phone(args[0])
            if phone:
                print(phone)
            else:
                print("Contact not found.")
        elif command == "all":
            contacts = book.all_records()
            for contact in contacts:
                print(contact)
        elif command == "add-birthday" and len(args) == 2:
            if book.add_birthday_to_contact(args[0], args[1]):
                print("Birthday added.")
            else:
                print("Error: Contact not found or invalid birthday format.")
        elif command == "show-birthday" and len(args) == 1:
            birthday = book.get_birthday(args[0])
            if birthday:
                print(birthday)
            else:
                print("Error: Contact not found or no birthday set.")
        elif command == "birthdays":
            upcoming_birthdays = book.get_birthdays_per_week()
            if upcoming_birthdays:
                for record in upcoming_birthdays:
                    print(record)
            else:
                print("No birthdays next week.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    