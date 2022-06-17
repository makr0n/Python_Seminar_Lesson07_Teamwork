# Процедуры работы с базой данных

import json

path_to_db = 'db.json'


def get_all_deals():  # Возвращает весь список дел из файла db.json
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        data = [data[i] for i in range(1, len(data))]
    return data

def get_one_deal(deal_id_get): # Возвращает одно дело по его deal_id
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        for i in range(1, len(data)): 
            if deal_id_get == data[i]['deal_id']:
                one_deal_get = data[i]
    return one_deal_get

def add_deal(deal_new):  # Добавление нового дела в БД {'deal_id': '', 'deal': 'Найти клад', 'deadline': '', 'status': 'новое'}
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        data[0]['id_counter'] +=1 # Увеличиваем id_counter на 1.               
        deal_new['deal_id'] = data[0]['id_counter'] # Присваиваем значение id_counter ключу deal_id
        data.append(deal_new)     # Добавляем в список словарей новое дело   
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file)
    return data

def change_deal(deal_edit):  # Изменение дела с deal_id = 6 в БД на {'deal_id': 6, 'deal': 'Найти клад', 'deadline': '30.06.2022', 'status': 'в работе'}
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)

        for i in range(1, len(data)): # Для изменения дела c deal_id = 6, находим в БД словарь с deal_id = 6 и перезаписываем его.
            if deal_edit['deal_id'] == data[i]['deal_id']:
                data[i] = deal_edit
        
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file)    
    return data


def clear_db(): # Очистка базы данных
    first_element = [{'id_counter': 0}, ]
    with open(path_to_db, 'w') as file:
        json.dump(first_element, file)

if __name__ == "__main__":
#    clear_db()

#Тестирование БД на тестовых данных test_data
    path_to_db = 'test_db.json'
    test_data = [{"id_counter": 5}, 
            {'deal_id': 1, 'deal': 'Помыть кота', 'deadline': '12.05.2022', 'status': 'выполнено'}, 
            {'deal_id': 2, 'deal': 'Постирать', 'deadline': '12.07.2022', 'status': 'просрочено'},
            {'deal_id': 3, 'deal': 'Лохматить бабушку', 'deadline': '20.07.2022', 'status': 'в работе'},
            {'deal_id': 4, 'deal': 'Написать To-do list', 'deadline': '16.07.2022', 'status': 'не выполнено'},
            {'deal_id': 5, 'deal': 'Съесть кактус', 'deadline': '', 'status': 'делать не буду'}]

    with open ('test_db.json', 'w') as test_file:
        json.dump(test_data,test_file)


    print('***get_all_deals()***')
    print(get_all_deals())

    print('***add_deal(test_deal_add)***')
    test_deal_add = {'deal_id': '', 'deal': 'Найти клад', 'deadline': '', 'status': 'новое'}
    print(add_deal(test_deal_add))

    print('***change_deal(test_deal_edit)***')
    test_deal_edit = {'deal_id': 6, 'deal': 'Найти клад', 'deadline': '29.06.2022', 'status': 'в работе'}
    print(change_deal(test_deal_edit))

    print('***get_one_deal(test_deal_id_get)***')
    test_deal_id_get = 3
    print(get_one_deal(test_deal_id_get))



# def change_deal(deal):  # Изменение
#     with open(path_to_db, 'r', encoding='UTF-8') as file:

#         #data = json.load(path_to_db)
#         #data = [data[i] for i in range(1, len(data))]
#         return data


# def del_deal():  # Удаление
#     data = json.load(path_to_db)
#     data = [data[i] for i in range(1, len(data))]
#     return data


# def get_undone_deals():  # Возврат невыполненных status=0
#     with open(path_to_db, 'r', encoding='UTF-8') as file:
#         data = json.load(file)
#         data = [data[i] for i in range(1, len(data)) if data[i]['status'] == 0]
#     return data


# def get_done_deals():  # Возврат выполненных status=1
#     with open(path_to_db, 'r', encoding='UTF-8') as file:
#         data = json.load(path_to_db)
#         data = [data[i] for i in range(1, len(data)) if data[i]['status'] == 1]
#     return data





# def change(deal, deal_id=-1):
#     with open('db.json', 'r') as file:
#         data = json.load(file)  # тип data должен быть list
#         if len(data) < 2:
#             return 'baseIsEmpty'
#     if deal_id == -1:
#         data.append(deal)
#     else:
#         -1  # внести в указанное дело изменения


# def get_data_undone():
#     with open('db.json', 'r') as file:
#         data = json.load(file)  # тип data должен быть list
#         if len(data) < 2:
#             return 'baseIsEmpty'
#     return [deal for deal in data if deal['status'] == 0]


def clear_db():
    first_element = [{'id_counter': 0}, ]
    with open('db.json', 'w') as file:
        json.dump(first_element, file)


if __name__ == "__main__":
     clear_db()
