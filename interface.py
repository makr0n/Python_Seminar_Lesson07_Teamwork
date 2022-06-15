main_menu = \
    'Выберите пункт меню:\n\
    1. \033[4mСписок всех дел\033[0m\n\
    2. \033[4mСписок незавершенных дел\033[0m\n\
    3. \033[4mСписок завершенных дел\033[0m\n\
    4. \033[4mДобавить дело\033[0m\n\
    5. \033[4mИзменить дело\033[0m\n\
    6. \033[4mВыход\033[0m'


def start_page():
    print('\033[3;36mСписок Дел v0.1\033[0m')
    print(50 * "=")
    print(main_menu)
    print(50 * "=")
    command = input('\033[1mВыберите действие: \033[0m')
    return command
start_page()


def show_deals(data):
    print('\033[4mСписок всех дел:\033[0m')
    print(data)
    start_page()
    return command
show_deals(1)

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
