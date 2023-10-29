import datetime
import pickle
from record import Record
from birthday import Birthday

class AddressBook:

    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def change_phone(self, name, new_phone):
        for record in self.records:
            if record.name == name:
                record.phone = new_phone
                return True
        return False

    def get_phone(self, name):
        for record in self.records:
            if record.name == name:
                return record.phone
        return None

    def all_records(self):
        return [str(record) for record in self.records]

    def add_birthday_to_contact(self, name, date):
        for record in self.records:
            if record.name == name:
                if Birthday.is_valid(date):
                    record.birthday = Birthday(date)
                    return True
        return False

    def get_birthday(self, name):
        for record in self.records:
            if record.name == name and record.birthday:
                return str(record.birthday)
        return None

    def get_birthdays_per_week(self):
        today = datetime.date.today()
        week_time = datetime.timedelta(days=7)
        upcoming_birthdays = []

        for record in self.records:
            if record.birthday:
                next_birthday = datetime.date(today.year, record.birthday.month, record.birthday.day)
                if today <= next_birthday <= today + week_time:
                    upcoming_birthdays.append(str(record))

        return upcoming_birthdays

    # модуль pickle
    def save_to_file(self, filename="addressbook.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.records, file)

    def load_from_file(self, filename="addressbook.pkl"):
        with open(filename, "rb") as file:
            self.records = pickle.load(file)
