import datetime
import json
import re


class Phone:
    def __init__(self, phone):
        self._phone = None
        self.phone = phone

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(value):
            raise ValueError("Телефон має складатися з 10 цифр.")
        self._phone = value

    def __str__(self):
        return self._phone


class Birthday:
    def __init__(self, birthday):
        self._birthday = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        pattern = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')
        if not pattern.match(value):
            raise ValueError("Дата народження має бути у форматі DD.MM.YYYY.")
        self._birthday = value

    def __str__(self):
        return self._birthday


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, phone, new_phone):
        for p in self.phones:
            if p.phone == phone:
                p.phone = new_phone

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def days_till_birthday(self):
        today = datetime.date.today()
        birth_date = datetime.datetime.strptime(self.birthday.birthday, "%d.%m.%Y").date()
        next_birthday = datetime.date(today.year, birth_date.month, birth_date.day)
        if today > next_birthday:
            next_birthday = datetime.date(today.year + 1, birth_date.month, birth_date.day)
        return (next_birthday - today).days

    def __str__(self):
        return f"{self.name}: {', '.join([str(phone) for phone in self.phones])}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def __contains__(self, name):
        return name in self.data

    def __getitem__(self, name):
        return self.data.get(name)

    def add_record(self, record):
        self.data[record.name] = record

    def find(self, name):
        return self.data.get(name)

    def get_birthdays_per_week(self):
        names_with_birthdays = []
        for name, record in self.data.items():
            if record.birthday and 0 <= record.days_till_birthday() < 7:
                names_with_birthdays.append(name)
        return names_with_birthdays

    def save_to_file(self):
        with open("addressbook.json", "w") as file:
            data_to_save = {}
            for name, record in self.data.items():
                phones = [phone.phone for phone in record.phones]
                birthday = record.birthday.birthday if record.birthday else None
                data_to_save[name] = {"phones": phones, "birthday": birthday}
            json.dump(data_to_save, file)

    def load_from_file(self):
        try:
            with open("addressbook.json", "r") as file:
                loaded_data = json.load(file)
                for name, data in loaded_data.items():
                    record = Record(name)
                    for phone in data["phones"]:
                        record.add_phone(phone)
                    if data["birthday"]:
                        record.add_birthday(data["birthday"])
                    self.add_record(record)
        except FileNotFoundError:
            pass
