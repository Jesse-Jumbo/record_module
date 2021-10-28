import json

if __name__ == '__main__':
    filename = 'save_data.json'

    with open(filename, 'r') as r_f:
        save_data = json.load(r_f)
        print(save_data)