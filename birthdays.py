from datetime import datetime, timedelta

class Birthday:
    def __init__(self, birthday_str):
        self.birthday = datetime.strptime(birthday_str, "%d.%m.%Y")

    def days_to_birthday(self):
        today = datetime.today()
        next_birthday = datetime(today.year, self.birthday.month, self.birthday.day)
        if today > next_birthday:
            next_birthday = datetime(today.year + 1, self.birthday.month, self.birthday.day)
        return (next_birthday - today).days
