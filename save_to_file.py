from results_record import Record
import json

# json 檔案儲存

if __name__ == '__main__':
    data_1 = Record("Jesse",  0)
    data_2 = Record("Jessie",  1)
    data_3 = Record("Jess",  2)
    data_4 = Record("Jessee",  3)
    data_5 = Record("Jessy",  4)
    data_6 = Record("jesse",  5)
    data_7 = Record("jessie",  6)
    data_8 = Record("jess",  7)
    data_9 = Record("jessee",  8)
    data_10 = Record("jessy",  9)
    filename = 'save_data.json'
    save_data = [{"id": data_1.id, "point": data_1.point},
                 {"id": data_2.id, "point": data_2.point},
                 {"id": data_3.id, "point": data_3.point},
                 {"id": data_4.id, "point": data_4.point},
                 {"id": data_5.id, "point": data_5.point},
                 {"id": data_6.id, "point": data_6.point},
                 {"id": data_7.id, "point": data_7.point},
                 {"id": data_8.id, "point": data_8.point},
                 {"id": data_9.id, "point": data_9.point},
                 {"id": data_10.id, "point": data_10.point}]

    with open(filename, 'w') as s_f:
        json.dump(save_data, s_f)
        print(save_data)


