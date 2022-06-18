import time

# import os

main_menu = \
    'Выберите пункт меню:\n\
    1. \033[4mСписок всех дел\033[0m\n\
    2. \033[4mСписок дел по статусу\033[0m\n\
    3. \033[4mДобавить дело\033[0m\n\
    4. \033[4mИзменить дело\033[0m\n\
    5. \033[4mВыход\033[0m'


def start_page():  # Starting page, choose number
    print('╔' + 48 * "=" + '╗')
    print('            \033[3;36mСписок Дел v0.1\033[0m')
    print('╚' + 48 * "=" + '╝')
    print(main_menu)
    print(50 * "=")
    print()
    command = input('\033[1mВыберите действие: \033[0m')
    print(50 * "•")
    return command


def show_deals(data):  # 1 in menu

    if data != []:

        print('\033[4mСписок всех дел:\033[0m')
        for item in range(len(data)):
            a = data[item]['deal_id']
            b = data[item]['deal']
            c = data[item]['deadline']
            d = data[item]['status']
            print(f'{a}) {b}. {c}. {d}. ')
        print(50 * "•")
    else:
        print('\033[33mСписок дел пуст\033[0m')


def show_deals_by_status():
    print('\033[4mВыберите статус дела для отображения:\033[0m')
    status = int(input('1-Новые, 2-В работе, 3-Отложенные, 4-Просроченные, 5-Выполенные'))
    print(50 * "=")
    return status


def finished_deals():
    print('\033[4mСписок законченных дел:\033[0m')
    #print(data)
    print(50 * "=")
    start_page()


def add_deal():
    print('\033[3mДобавление дела\033[0m')
    print(50 * "-")
    deal_name = input('Что необходимо сделать: ')  # plain text
    deal_deadline = input('Укажите сроки выполнения в формате ДД-ММ-ГГ: ')  # DD-MM-YY
    deal = {'deal_id': -1, 'deal': deal_name, 'deadline': deal_deadline, 'status': 1}
    deal['status'] = 1
    return deal


def change_deal():
    print('\033[4mИзменение дела:\033[0m')
    print(50 * "~")
    deal_id = input('Выберите номер дела которого необходимо изменить:')
    return int(deal_id)


def change_deal_content(one_deal):
    command = input('Что необходимо сделать:\n 1 - Изменить статус \n 2 - Изменить содержание \n 3 - Удалить дело')
    if command == '1':
        status = (input('1-Новые, 2-В работе, 3-Отложенные, 4-Просроченные, 5-Выполенные'))
        one_deal['status'] = int(status)
    elif command == '2':
        one_deal['deal'] = (input('Новое описание дела: '))
    elif command == '3':
        one_deal['status'] = 10 #Статус дела на удаление
    return one_deal


def bye_mess():  # 6 in menu
    print('Работа завершена!')


def error_input():
    print('\033[5;31mОшибка!\033[0m')
    print('\033[21mПожалуйста введите число, соответствующее пункту меню.\033[0m')
    time.sleep(2)
    start_page()


def done_message():
    print('Выполнено!')

