# CK special selection point record
import json

class Record:
    def __init__(self, id: str, point: int):
        self.id = id
        self.point = point

class RecordManager:
    def __init__(self):
        self.data = []
        self.filename = "data.json"
    #創黨

    def add(self, record: Record):
        with open(self.filename, 'r') as f:
            self.data = json.load(f)
        with open(self.filename, 'w') as f:
            self.data.append(record.__dict__)
            json.dump(self.data, f)

    def get_all(self) -> list:
        with open(self.filename, 'r') as f:
            data = json.load(f)
        return data

    def get(self, user_id: str) -> list:
        result = []
        with open(self.filename, 'r') as f:
            data = json.load(f)
        for x in data:
            if user_id == x["id"]:
                result.append(x)
            else:
                print("no found")
        return result


