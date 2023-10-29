from address_book import AddressBook, Record, Name, Phone, Date

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error: {e}"
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Wrong number of parameters."
        except Exception as e:
            return f"Unknown error: {e}"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.lower(), args

@input_error
def add_contact(args, address_book):
    name, phone = args
    if address_book.find(name):
        return f"Contact {name} already exists."
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return "Contact added."

@input_error
def change_contact(args, address_book):
    name, phone = args
    record = address_book.find(name)
    if record:
        record.edit_phone(record.phones[0].value, phone)
        return f"Phone for {name} changed."
    else:
        return f"User {name} not found."

@input_error
def get_phone(args, address_book):
    name = args[0]
    record = address_book.find(name)
    if record:
        return record.phones[0].value
    else:
        return f"No phone for {name} found."

@input_error
def add_birthday(args, address_book):
    name, date = args
    record = address_book.find(name)
    if record:
        record.set_birthday(date)
        return f"Birthday for {name} set."
    else:
        return f"User {name} not found."

@input_error
def show_birthday(args, address_book):
    name = args[0]
    record = address_book.find(name)
    if record and record.birthday:
        return record.birthday.value
    else:
        return f"No birthday for {name} found."

def show_all_contacts(address_book):
    return '\n'.join([str(record) for record in address_book.values()])

def main():
    address_book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            print(add_contact(args, address_book))
        elif command == "change" and len(args) == 2:
            print(change_contact(args, address_book))
        elif command == "phone" and len(args) == 1:
            print(get_phone(args, address_book))
        elif command == "add-birthday" and len(args) == 2:
            print(add_birthday(args, address_book))
        elif command == "show-birthday" and len(args) == 1:
            print(show_birthday(args, address_book))
        elif command == "all":
            print(show_all_contacts(address_book))
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
