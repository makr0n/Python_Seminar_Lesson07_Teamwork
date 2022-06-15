import time

main_menu = \
    'Выберите пункт меню:\n\
    1. \033[4mСписок всех дел\033[0m\n\
    2. \033[4mСписок незавершенных дел\033[0m\n\
    3. \033[4mСписок завершенных дел\033[0m\n\
    4. \033[4mДобавить дело\033[0m\n\
    5. \033[4mИзменить дело\033[0m\n\
    6. \033[4mВыход\033[0m'


def start_page():  # Starting page, choose number
    print('            \033[3;36mСписок Дел v0.1\033[0m')
    print(50 * "=")
    print(main_menu)
    print(50 * "=")
    command = int(input('\033[1mВыберите действие: \033[0m'))
    print(50 * "=")
    return command


def show_deals(data):  # 1 in menu
    print('\033[4mСписок всех дел:\033[0m')
    print(data)
    print(50 * "=")
    start_page()


def unfinished_deals():
    print('\033[4mСписок текущих дел:\033[0m')
    print(data)
    print(50 * "=")


def finished_deals():  # 4 in menu
    print('\033[4mСписок законченных дел:\033[0m')
    print(data)
    print(50 * "=")
    start_page()


def add_deal():
    print('\033[3mДобавление дела\033[0m')
    print(50 * "=")
    deal_name = input('Что необходимо сделать: ')  # plain text
    deal_deadline = input('Сроки выполнения: ')  # DD-MM-YYYY
    deal = deal_name + deal_deadline
    return deal


def change_deal():
    print('\033[4mИзменение дела:\033[0m')
    print(50 * "~")
    show_deals(data)
    deal_id = input('Выберите дело:')
    command = input('Что сделать: 1 - завершить, 2 - изменить, 3 - удалить')
    return command, deal_id


def bye_mess(): #6 in menu
    print('Работа завершена!')


def result_message(result):
    print('ok') if result == True else print('error')


def error_input():
    print('\033[5;31mОшибка!\033[0m')
    print('\033[21mПожалуйста введите число, соответствующее пункту меню.\033[0m')
    time.sleep(2)
    start_page()
