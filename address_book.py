from collections import UserDict
import re
import datetime

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value=None):
        if value and self.validate(value):
            super().__init__(value)
        else:
            self.value = None

    @staticmethod
    def validate(phone):
        return bool(re.fullmatch(r"\d{10}", phone))

class Birthday(Field):
    def __init__(self, value=None):
        if value and self.validate(value):
            super().__init__(value)
        else:
            self.value = None

    @staticmethod
    def validate(value):
        if re.match(r"^\d{2}\.\d{2}\.\d{4}$", value):
            day, month, year = map(int, value.split('.'))
            try:
                datetime.date(year, month, day)
                return True
            except ValueError:
                return False
        return False

class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.phone = Phone(phone)
        if birthday:
            self.birthday = Birthday(birthday)
    
    def add_phone(self, phone):
        self.phone = Phone(phone)

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def show_birthday(self):
        if hasattr(self, 'birthday'):
            return self.birthday.value
        return "No birthday set."

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def birthdays_next_week(self):
        birthdays_data = {}
        for name, record in self.data.items():
            if hasattr(record, 'birthday'):
                birthdays_data[name] = record.birthday.value
        return self.get_birthdays_per_week(birthdays_data)

    @staticmethod
    def get_birthdays_per_week(birthdays):
        today = datetime.datetime.now()
        week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        weekly_birthdays = {day: [] for day in week_days}

        for name, date_str in birthdays.items():
            birth_date = datetime.datetime.strptime(date_str, '%d.%m.%Y').replace(year=today.year)
            
            if birth_date < today:
                birth_date = birth_date.replace(year=today.year + 1)
            
            day_of_week = week_days[birth_date.weekday()]
            
            if day_of_week == "Saturday" or day_of_week == "Sunday":
                day_of_week = "Monday"
            
            weekly_birthdays[day_of_week].append(name)
        
        result = {}
        for i in range(7):
            current_day = week_days[(today.weekday() + i) % 7]
            if weekly_birthdays[current_day]:
                result[current_day] = ", ".join(weekly_birthdays[current_day])

        return result

