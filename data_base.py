# Процедуры работы с базой данных

import json

data = [{'deal_id': 1, 'deal': 'Помыть кота', 'deadline': '12.05.2022', 'status': 1}, {
    'deal_id': 2, 'deal': 'Постирать', 'deadline': '12.07.2022', 'status': 0}]

path_to_db = 'db.json'


def get_all_deals():  # Возвращает весь список дел из файла db.json
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        data = [data[i] for i in range(1, len(data))]
    return data


def add_deal():  # Добавление
    data = json.load(path_to_db)
    data = [data[i] for i in range(1, len(data))]
    return data


def change_deal(deal):  # Изменение
    with open(path_to_db, 'r', encoding='UTF-8') as file:

        #data = json.load(path_to_db)
        #data = [data[i] for i in range(1, len(data))]
        return data


def del_deal():  # Удаление
    data = json.load(path_to_db)
    data = [data[i] for i in range(1, len(data))]
    return data


def get_undone_deals():  # Возврат невыполненных status=0
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        data = [data[i] for i in range(1, len(data)) if data[i]['status'] == 0]
    return data


def get_done_deals():  # Возврат выполненных status=1
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(path_to_db)
        data = [data[i] for i in range(1, len(data)) if data[i]['status'] == 1]
    return data





def change(deal, deal_id=-1):
    with open('db.json', 'r') as file:
        data = json.load(file)  # тип data должен быть list
        if len(data) < 2:
            return 'baseIsEmpty'
    if deal_id == -1:
        data.append(deal)
    else:
        -1  # внести в указанное дело изменения


def get_data_undone():
    with open('db.json', 'r') as file:
        data = json.load(file)  # тип data должен быть list
        if len(data) < 2:
            return 'baseIsEmpty'
    return [deal for deal in data if deal['status'] == 0]


def clear_db():
    first_element = [{'id_counter': 0}, ]
    with open('db.json', 'w') as file:
        json.dump(first_element, file)


if __name__ == "__main__":
    clear_db()
