import json

class Phone:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phone = Phone(phone)

    def __str__(self):
        return f"{self.name}: {self.phone}"

class AddressBook:
    def __init__(self):
        self.records = []
        self.load_data()

    def load_data(self):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                for item in data:
                    record = Record(item['name'], item['phone'])
                    self.records.append(record)
        except FileNotFoundError:
            pass

    def save_data(self):
        data = [{"name": record.name, "phone": str(record.phone)} for record in self.records]
        with open("data.json", "w") as f:
            json.dump(data, f)

    def add_record(self, record):
        self.records.append(record)
        self.save_data()

    def change_phone(self, name, new_phone):
        for record in self.records:
            if record.name == name:
                record.phone = Phone(new_phone)
                self.save_data()
                return True
        return False

    def find_phone(self, name):
        for record in self.records:
            if record.name == name:
                return str(record.phone)
        return None

    def show_all_records(self):
        return "\n".join([str(record) for record in self.records])
