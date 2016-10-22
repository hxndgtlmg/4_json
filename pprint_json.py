import json


def load_data(filepath):
    with open(filepath) as file:
        data = json.loads(file.read())
    return data


def pretty_print_json(data):
    return json.dumps(data, sort_keys=True, indent=4)


if __name__ == '__main__':
    data = load_data(input("Введите путь к файлу: "))
    print(pretty_print_json(data))
