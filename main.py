from address_book import AddressBook, Record, Phone, Birthday

def main():
    book = AddressBook()

    while True:
        command = input("Enter command: ")

        if command in ['close', 'exit']:
            break

        elif command == 'hello':
            print("Hello!")

        elif command.startswith('add '):
            _, name, number = command.split()
            phone = Phone(number)
            record = Record(name, phone)
            book.add_record(record)

        elif command.startswith('change '):
            _, name, number = command.split()
            phone = Phone(number)
            record = book.find_record(name)
            if record:
                record.update_phone(phone)
            else:
                print(f"No contact named {name} found")

        elif command.startswith('phone '):
            _, name = command.split()
            record = book.find_record(name)
            if record:
                print(record.phones[0])
            else:
                print(f"No contact named {name} found")

        elif command == 'all':
            for record in book.records:
                print(record.name, record.phones[0])

        elif command.startswith('add-birthday '):
            _, name, date = command.split()
            birthday = Birthday(date)
            record = book.find_record(name)
            if record:
                record.birthday = birthday
            else:
                print(f"No contact named {name} found")

        elif command.startswith('show-birthday '):
            _, name = command.split()
            record = book.find_record(name)
            if record and record.birthday:
                print(record.birthday.date)
            else:
                print(f"No birthday for {name} found")

        elif command == 'birthdays':
            birthdays = book.get_birthdays_per_week()
            for day, names in birthdays.items():
                print(f"{day}: {names}")

        else:
            print("Unknown command")

main()
