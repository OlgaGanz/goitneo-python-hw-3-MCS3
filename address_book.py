import re
from datetime import datetime
from birthdays import get_birthdays_per_week

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def has_contact(self, name):
        return any(record.name == name for record in self.records)

    def get_phone(self, name):
        for record in self.records:
            if record.name == name:
                return record.phone.number
        return None

    def change_phone(self, name, new_phone):
        for record in self.records:
            if record.name == name:
                record.phone.number = new_phone

    def add_birthday(self, name, birthday):
        for record in self.records:
            if record.name == name:
                record.birthday = Birthday(birthday)

    def show_birthday(self, name):
        for record in self.records:
            if record.name == name:
                return record.birthday.date if record.birthday else None
        return None

    def birthdays_next_week(self):
        birthdays = {record.name: record.birthday.date for record in self.records if record.birthday}
        return get_birthdays_per_week(birthdays)

    def show_all(self):
        return {record.name: record.phone.number for record in self.records}

class Record:
    def __init__(self, name):
        self.name = name
        self.phone = None
        self.birthday = None

    def add_phone(self, number):
        self.phone = Phone(number)

    def add_birthday(self, date):
        self.birthday = Birthday(date)

class Phone:
    def __init__(self, number):
        self._number = None
        self.number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if re.match(r"^\d{10}$", value):
            self._number = value
        else:
            raise ValueError("Phone number must contain exactly 10 digits.")

class Birthday:
    def __init__(self, date):
        self._date = None
        self.date = date

    @property
    def date(self):
        return self._date.strftime('%d.%m.%Y')

    @date.setter
    def date(self, value):
        try:
            self._date = datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Date format must be DD.MM.YYYY")
