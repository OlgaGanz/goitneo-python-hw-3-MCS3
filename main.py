import pickle
from address_book import AddressBook, Record, Phone, Birthday
from birthdays import get_birthdays_per_week

def save_to_disk(book, filename='address_book.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(book, file)

def load_from_disk(filename='address_book.pkl'):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_from_disk()

    while True:
        try:
            command_input = input("Enter command: ").strip().lower()
            command_parts = command_input.split()

            if not command_parts:
                print("Please enter a command.")
                continue

            command = command_parts[0]

            if command == "add":
                name = command_parts[1]
                phone_number = command_parts[2]
                book.add_record(Record(name, Phone(phone_number)))
                print(f"Added {name} with phone number {phone_number}.")

            elif command == "change":
                name = command_parts[1]
                new_phone_number = command_parts[2]
                book.change_phone(name, new_phone_number)
                print(f"Phone number for {name} has been updated.")

            elif command == "phone":
                name = command_parts[1]
                phone_number = book.find_phone(name)
                print(f"Phone number for {name}: {phone_number}.")

            elif command == "all":
                records = book.show_all_records()
                for record in records:
                    print(record)

            elif command == "add-birthday":
                name = command_parts[1]
                birth_date = command_parts[2]
                book.add_birthday(name, Birthday(birth_date))
                print(f"Birthday for {name} added.")

            elif command == "show-birthday":
                name = command_parts[1]
                birthday = book.show_birthday(name)
                print(f"Birthday for {name}: {birthday}.")

            elif command == "birthdays":
                birthdays = book.collect_birthdays()
                results = get_birthdays_per_week(birthdays)
                for day, names in results.items():
                    print(f"{day}: {names}")

            elif command == "hello":
                print("Hello! How can I assist you today?")

            elif command in ["close", "exit"]:
                save_to_disk(book)
                print("Goodbye!")
                break

            else:
                print("Unknown command. Please try again.")

        except (ValueError, IndexError) as e:
            print(e)

if __name__ == "__main__":
    main()
