import json
from results_record import Record

if __name__ == '__main__':
    filename = 'save_data.json'
    data_11 = Record(id="new_data", point=10)
    write_data = [{"id": data_11.id, "point": data_11.point}]

    with open(filename, 'r') as r_f:
        save_data = json.load(r_f)
        print(save_data)

    with open(filename, 'w') as w_f:
        new_data = save_data + write_data
        json.dump(new_data, w_f)
        print(new_data)