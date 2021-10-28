# CK special selection result record

class Record:
    def __init__(self, id: str, point: int):
        self.id = id            # 單個學生ID
        self.point = point    # 單個學生成績

class Method(Record):
    def __init__(self):
        Record.__init__(self)

    def add(self, name, result):
        self.id.append(name)                                        # 將輸入的名字加到學生ID的最後一項
        self.result.append(result)                                  # 將輸入的成績加到學生成績的最後一項
        for x in self.id:                                           # 創建一個迴圈存取學生ID
            for y in self.result:                                   # 創建一個迴圈存取學生成績
                self.all_result[self.id[x]] = self.result[y]    # 將學生成績字典的key設為學生ID，value設為學生成績
                if y == " ":                                            # 如果已經到學生成績的最後一項了，就跳到下一個學生ID的學生成績
                    break
            self.all_data.append(self.all_result)                       # 將學生成績字典添加到所有學生成績列表的最後一項

    def all(self):
        return self.all_data                                            # 回傳所有學生和他所有的成績

    def get(self, search_id):
        for x in self.all_result:                                       # 創建一個迴圈尋找學生成績字典的key
            if self.all_result[x] != search_id:                         # 如果輸入的ID不符合學生成績字典內的ID
                print("查無此人")                                        # 輸出以下文字
            else:                                                       # 否則
                print("以下是", search_id, "的所有成績: ")                 # 輸出輸入的ID的所有成績
                return self.all_result.get(search_id)                   # 回傳輸入的學生ID在學生成績字典裡找到的所有成績

r = Record()
