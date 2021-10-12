import json


def load_json(file_path_name):
    file_path = '../data/' + file_path_name
    with open(
            file_path,
            "r",
            encoding="utf-8"
    ) as f:
        return json.load(f)


if __name__ == '__main__':
    filepath = "login.json"
    load_json = load_json(file_path_name=filepath)

    print(load_json)
