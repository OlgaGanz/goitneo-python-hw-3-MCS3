import pickle
from datetime import datetime, timedelta
import re

class Phone:
    def __init__(self, phone_number):
        self.phone = self._validate_phone(phone_number)

    def _validate_phone(self, phone_number):
        if not re.match(r"^\d{10}$", phone_number):
            raise ValueError("Phone number must consist of 10 digits")
        return phone_number

    def __str__(self):
        return self.phone

class Birthday:
    def __init__(self, birthday_date):
        self.birthday = self._validate_birthday(birthday_date)

    def _validate_birthday(self, birthday_date):
        try:
            birthday = datetime.strptime(birthday_date, '%d.%m.%Y').date()
            if birthday > datetime.now().date():
                raise ValueError("Birthday date cannot be in the future.")
            return birthday
        except ValueError:
            raise ValueError("Invalid birthday format. Expected DD.MM.YYYY")

class Record:
    def __init__(self, name, phone_number=None, birthday_date=None):
        self.name = name
        self.phones = []
        if phone_number:
            self.add_phone(phone_number)
        self.birthday = None
        if birthday_date:
            self.add_birthday(birthday_date)

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def add_birthday(self, birthday_date):
        self.birthday = Birthday(birthday_date)

    def days_to_birthday(self):
        if not self.birthday:
            return None

        today = datetime.now().date()
        next_birthday = datetime(today.year, self.birthday.birthday.month, self.birthday.birthday.day).date()

        if today > next_birthday:
            next_birthday = datetime(today.year + 1, self.birthday.birthday.month, self.birthday.birthday.day).date()

        return (next_birthday - today).days

    def __str__(self):
        phones = "\n".join([str(phone) for phone in self.phones])
        return f"{self.name}\n{phones}"

class AddressBook:
    def __init__(self):
        self.book = []

    def add_record(self, record):
        self.book.append(record)

    def change_phone(self, name, new_phone):
        for record in self.book:
            if record.name == name:
                record.phones = [Phone(new_phone)]

    def get_record(self, name):
        for record in self.book:
            if record.name == name:
                return record

    def get_phone(self, name):
        record = self.get_record(name)
        if record and record.phones:
            return str(record.phones[0])

    def get_birthday(self, name):
        record = self.get_record(name)
        if record and record.birthday:
            return record.birthday.birthday.strftime('%d.%m.%Y')

    def get_birthdays_per_week(self):
        users_to_congratulate = {}
        for record in self.book:
            days_to_birthday = record.days_to_birthday()
            if days_to_birthday is not None and days_to_birthday <= 7:
                users_to_congratulate[record.name] = days_to_birthday
        return users_to_congratulate

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.book, file)

    def load(self, filename):
        with open(filename, 'rb') as file:
            self.book = pickle.load(file)
