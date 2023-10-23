import pickle

class Phone:
    def __init__(self, phone):
        if not (phone.isdigit() and len(phone) == 10):
            raise ValueError("Phone number must be 10 digits.")
        self.phone = phone

class Name:
    def __init__(self, name):
        self.name = name

class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phones = [Phone(phone)]
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday_obj):
        self.birthday = birthday_obj

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, name, phone):
        if name in self.data:
            self.data[name].add_phone(phone)
        else:
            self.data[name] = Record(name, phone)

    def find(self, name):
        return self.data.get(name, None)

    def get_birthdays_per_week(self):
        upcoming = {}
        for name, record in self.data.items():
            if record.birthday and record.birthday.days_to_birthday() <= 7:
                upcoming[name] = record.birthday.days_to_birthday()
        return upcoming

    def save_to_file(self, filename="address_book.pkl"):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load_from_file(cls, filename="address_book.pkl"):
        with open(filename, 'rb') as file:
            address_book = pickle.load(file)
        return address_book
