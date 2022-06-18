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
        one_deal_get = {}
        for i in range(1, len(data)): 
            if deal_id_get == data[i]['deal_id']:
                one_deal_get = data[i]
    return one_deal_get

def get_status_deal(deal_status_get): # Возвращает список дел по значению status
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        status_deal_get = []
        for i in range(1, len(data)): 
            if  data[i]['status'] == deal_status_get:
                status_deal_get.append(data[i])
    return status_deal_get

def add_deal(deal_new):  # Добавление нового дела в БД {'deal_id': '', 'deal': 'Найти клад', 'deadline': '', 'status': 'новое'}
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        data[0]['id_counter'] +=1 # Увеличиваем id_counter на 1.               
        deal_new['deal_id'] = data[0]['id_counter'] # Присваиваем значение id_counter ключу deal_id
        data.append(deal_new)     # Добавляем в список словарей новое дело   
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file)
    #return data

def change_deal(deal_edit):  # Изменение дела 
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)

        for i in range(1, len(data)): # Для изменения дела c deal_id = 6, находим в БД словарь с deal_id = 6 и перезаписываем его.
            if deal_edit['deal_id'] == data[i]['deal_id']:
                data[i] = deal_edit
        
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file)    
    #return data

def delete_deal(deal_id_delete): # Удаление дела в БД по его deal_id
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
                  
        for i in range(1, len(data)): 
            if data[i]['deal_id'] == deal_id_delete: # находим индекс элемента в списке словарей с нужным deal_id
                index_del = i
        data.pop(index_del)   # Удаляем из списка словарь с нужным deal_id
        for i in range(1, len(data)): # Перезаписаваем в каждом словаре списка ключ deal_id
            data[i]['deal_id'] = i
        
        data[0]['id_counter'] -= 1 # Уменьшаем id_counter на 1
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file)    
    #return data

def clear_db(path_to_db): # Очистка базы данных
    first_element = [{'id_counter': 0}, ]
    with open(path_to_db, 'w') as file:
        json.dump(first_element, file)

if __name__ == "__main__":
#Тестирование БД на тестовых данных test_data
    from pprint import pprint
    path_to_db = 'test_db.json'
    clear_db(path_to_db)
    test_data = [{"id_counter": 5}, 
            {'deal_id': 1, 'deal': 'Помыть кота', 'deadline': '12.05.2022', 'status': 'выполнено'}, 
            {'deal_id': 2, 'deal': 'Постирать', 'deadline': '12.07.2022', 'status': 'просрочено'},
            {'deal_id': 3, 'deal': 'Лохматить бабушку', 'deadline': '20.07.2022', 'status': 'в работе'},
            {'deal_id': 4, 'deal': 'Написать To-do list', 'deadline': '16.07.2022', 'status': 'не выполнено'},
            {'deal_id': 5, 'deal': 'Съесть кактус', 'deadline': '', 'status': 'делать не буду'}]

    with open (path_to_db, 'w') as test_file:
        json.dump(test_data,test_file)

    print('')
    print('***get_all_deals()***')
    pprint(get_all_deals(), sort_dicts=False)

    print('')
    print('***add_deal(test_deal_add)***')
    test_deal_add = {'deal_id': '', 'deal': 'Найти клад', 'deadline': '', 'status': 'новое'}
    print('***')
    print(test_deal_add)    
    print('***')    
    add_deal(test_deal_add)
    with open (path_to_db, 'r') as test_file:
        text = json.load(test_file)
        pprint(text, sort_dicts=False)

    print('')
    print('***change_deal(test_deal_edit)***')
    test_deal_edit = {'deal_id': 6, 'deal': 'Найти клад', 'deadline': '29.06.2022', 'status': 'в работе'}
    change_deal(test_deal_edit)
    with open (path_to_db, 'r') as test_file:
        text = json.load(test_file)
        pprint(text, sort_dicts=False)

    print('')
    print('***get_one_deal(test_deal_id_get)***')
    test_deal_id_get = 3
    print(get_one_deal(test_deal_id_get))

    print('')
    print('***delete_deal(deal_delete)***')
    test_deal_id_delete = 5
    print('***')
    print(get_one_deal(test_deal_id_delete))
    print('***')
    delete_deal(test_deal_id_delete)
    with open (path_to_db, 'r') as test_file:
        text = json.load(test_file)
        pprint(text, sort_dicts=False)
        
    print('')
    print('***get_status_deal(deal_status_get)***')
    print('***')
    deal_status_get = 'выполнено'
    print(deal_status_get)
    print('***')
    pprint(get_status_deal(deal_status_get), sort_dicts=False)