from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Phone number must have 10 digits.")
        super().__init__(value)

    @staticmethod
    def validate(value):
        return len(value) == 10 and value.isdigit()

class Birthday(Field):
    def __init__(self, date_str):
        if not self.validate(date_str):
            raise ValueError("Date format must be DD.MM.YYYY")
        super().__init__(datetime.strptime(date_str, "%d.%m.%Y"))

    @staticmethod
    def validate(date_str):
        try:
            datetime.strptime(date_str, "%d.%m.%Y")
            return True
        except:
            return False

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for idx, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[idx] = Phone(new_phone)

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def birthdays_for_next_week(self):
        today = datetime.now()
        upcoming_week = [(today + timedelta(days=i)).date() for i in range(7)]
        upcoming_birthdays = [(name, record.birthday.value.date()) for name, record in self.data.items() if record.birthday and record.birthday.value.date() in upcoming_week]
        return upcoming_birthdays
