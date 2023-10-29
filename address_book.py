import json
from datetime import datetime, timedelta

class AddressBook:
    def __init__(self):
        self.records = []
        self.load_data()

    def add_record(self, record):
        self.records.append(record)
        self.save_data()

    def change_phone(self, name, new_phone):
        for record in self.records:
            if record.name == name:
                record.phone = new_phone
        self.save_data()

    def show_phone(self, name):
        for record in self.records:
            if record.name == name:
                return record.phone
        return None

    def show_all(self):
        return self.records

    def add_birthday(self, name, birthday):
        for record in self.records:
            if record.name == name:
                record.birthday = birthday
        self.save_data()

    def show_birthday(self, name):
        for record in self.records:
            if record.name == name:
                return record.birthday
        return None

    def birthdays_per_week(self):
        today = datetime.now().date()
        upcoming_birthdays = []
        for record in self.records:
            if record.birthday:
                bd_date = datetime.strptime(record.birthday, "%d.%m.%Y").date().replace(year=today.year)
                if today <= bd_date < today + timedelta(days=7):
                    upcoming_birthdays.append((record.name, record.birthday))
        return upcoming_birthdays

    def save_data(self):
        data = [{"name": record.name, "phones": [record.phone], "birthday": record.birthday} for record in self.records]
        with open('storage.json', 'w') as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open('storage.json', 'r') as f:
                data = f.read()
                if data:
                    data = json.loads(data)
                    for item in data:
                        phones = [Phone(phone) for phone in item['phones']]
                        birthday = Birthday(item['birthday']) if item['birthday'] else None
                        record = Record(item['name'], phones[0] if phones else None, birthday)
                        self.records.append(record)
        except FileNotFoundError:
            pass


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.birthday}"


class Phone:
    def __init__(self, phone):
        self.phone = phone

    def __str__(self):
        return self.phone


class Birthday:
    def __init__(self, birthday):
        self.birthday = birthday

    def __str__(self):
        return self.birthday
