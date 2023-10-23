from address_book import AddressBook, Phone, Record
from birthdays import Birthday

book = AddressBook()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError):
            return "Invalid input. Please check and try again."
    return inner

@input_error
def add_contact(args):
    name, phone = args.split()
    book.add_record(name, phone)
    return "Contact added."

@input_error
def change_contact(args):
    name, phone = args.split()
    if name in book.data:
        book.data[name].phones = [Phone(phone)]
        return f"Phone for {name} changed."
    return "Contact not found."

@input_error
def phone(args):
    name = args.strip()
    if name in book.data:
        return ", ".join([p.phone for p in book.data[name].phones])
    return "Contact not found."

@input_error
def all_contacts(args):
    return "\n".join([f"{name}: {', '.join([p.phone for p in record.phones])}" for name, record in book.data.items()])

@input_error
def add_birthday(args):
    name, date = args.split()
    if name in book.data:
        book.data[name].add_birthday(Birthday(date))
        return f"Birthday added for {name}."
    return "Contact not found."

@input_error
def show_birthday(args):
    name = args.strip()
    if name in book.data and book.data[name].birthday:
        return str(book.data[name].birthday.birthday.date())
    return "Birthday not found for this contact."

def birthdays(args):
    upcoming = book.get_birthdays_per_week()
    if upcoming:
        return "\n".join([f"{name} has a birthday in {days} days" for name, days in upcoming.items()])
    return "No birthdays in the upcoming week."

def hello(args):
    return "Hello! How can I assist you?"

def close(args):
    book.save_to_file()
    exit()

def main():
    command_dict = {
        'add': add_contact,
        'change': change_contact,
        'phone': phone,
        'all': all_contacts,
        'add-birthday': add_birthday,
        'show-birthday': show_birthday,
        'birthdays': birthdays,
        'hello': hello,
        'close': close,
        'exit': close
    }

    try:
        book = AddressBook.load_from_file()
    except:
        book = AddressBook()

    while True:
        user_input = input("Enter command: ").strip()
        command, *args = user_input.split(' ', 1)
        args = args[0] if args else ''
        if command in command_dict:
            print(command_dict[command](args))
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
