

main_menu = \
'Выберите пункт меню:\n\
1. Список всех дел\n\
2. Список незавершенных дел\n\
3. Список завершенных дел\n\
4. Добавить дело\n\
5. Изменить дело\n\
6. Выход'



def start_page():
    print (main_menu)
    command = input('message: ')
    return command

def show_deals(data):
    print(data)
    command = input('message: ')
    return command

def add_deal():
    deal_name = input('message: ')
    deal_deadline = input('message: ')
    deal = deal_name + deal_deadline
    return deal

def change_deal():
    deal_id = input('message: ')
    command = input('Что сделать: 1 - завершить, 2 - изменить, 3 - удалить')
    return command, deal_id

def result_message(result):
    print('ok') if result == True else print('error')
