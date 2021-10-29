# CK special selection point record

class Record:
    def __init__(self, id: str, point: int):
        self.id = id
        self.point = point

class Method():
    def __init__(self, id, point):
        self.record = Record()
        self.record.id = id
        self.record.point = point

    def add(self, id: str, point: int):
        self.record.id += id
        self.record.point += point

    def all(self):
        return {"id": self.record.id, "point": self.record.point}

    def get(self, search_id):
        for x in self.record.id:
            for y in self.record.point:
                if self.record.id[x] != search_id:
                    print("查無此人")
                else:
                    print("以下是", search_id, "的所有成績: ")
                    self.record.id[x] = search_id
                    return {"id": search_id, "point": self.record.point[y]}
