from addressbook import AddressBook, Record

def main():
    book = AddressBook()
    book.load_from_file()

    while True:
        try:
            command = input("> ").split()
            action = command[0]

            if action == "add":
                name = command[1]
                phone = command[2]
                record = Record(name)
                record.add_phone(phone)
                book.add_record(record)
                print(f"Контакт {name} успішно додано!")

            elif action == "change":
                name = command[1]
                phone = command[2]
                if name in book:
                    book[name].edit_phone(book[name].phones[0].phone, phone)
                    print(f"Номер телефону для {name} змінено на {phone}!")

            elif action == "phone":
                name = command[1]
                if name in book:
                    print(book.find(name))
                else:
