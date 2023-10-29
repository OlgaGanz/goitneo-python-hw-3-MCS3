import pickle
from address_book import AddressBook, Record

def parse_input(user_input):
    parts = user_input.split()
    command = parts[0]
    args = parts[1:]
    return command, args

def save_to_disk(book, filename='addressbook.dat'):
    with open(filename, 'wb') as f:
        pickle.dump(book, f)

def load_from_disk(filename='addressbook.dat'):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_from_disk()  
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "add":
            name, phone = args
            record = Record(name)
            record.add_phone(phone)
            book.add_record(record)
            print(f"Added {name} with phone number {phone}.")

        elif command == "change":
            name, phone = args
            record = book.find(name)
            if record:
                record.edit_phone(record.phones[0].value, phone)
                print(f"Changed phone number for {name} to {phone}.")
            else:
                print(f"{name} not found.")

        elif command == "phone":
            name = args[0]
            record = book.find(name)
            if record:
                print(f"Phone number for {name}: {record.phones[0]}")
            else:
                print(f"{name} not found.")

        elif command == "all":
            for name, record in book.data.items():
                print(record)

        elif command == "add-birthday":
            name, date = args
            record = book.find(name)
            if record:
                record.add_birthday(date)
                print(f"Added birthday for {name} on {date}.")
            else:
                print(f"{name} not found.")

        elif command == "show-birthday":
            name = args[0]
            record = book.find(name)
            if record and record.birthday:
                print(f"Birthday for {name}: {record.birthday.value.date()}")
            else:
                print(f"{name} does not have a birthday set or not found.")

        elif command == "birthdays":
            birthdays = book.birthdays_for_next_week()
            if birthdays:
                print(f"Upcoming birthdays for the next week: {', '.join([name for name, _ in birthdays])}")
            else:
                print("No birthdays in the next week.")

        elif command == "hello":
            print("Hello! How can I assist you today?")

        elif command in ["close", "exit"]:
            save_to_disk(book)  
            print("Good bye!")
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
