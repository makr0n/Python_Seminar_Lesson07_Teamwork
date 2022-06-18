import interface
import data_base
import logger


def run():
    
    while True:
    
        command = interface.start_page()

        match command:
            case '1':     # Список всех дел
                data = data_base.get_all_deals() ## прошу дописать функцию в data_base
                interface.show_deals(data) ## предлагаю не вводить команду юзера, а после вывода дел вызывать главное меню + дописать исключение, если 'baseIsEmpty'

            case '2': # Список дел по статусу
                status = -1
                data = data_base.get_status_deal(status) ## прошу переименовать функцию get_data_undone в data_base
                interface.show_deals(data)
            
            case '3': # Список завершенных дел
                data = data_base.get_done_deals() ## прошу дописать функцию get_done_deals в data_base
                interface.show_deals(data)
            
            case '4': # Добавить дело
                deal_id = -1
                user_data = interface.add_deal() # user_data - введенные юзером данные в удобном формате. Здесь я их преобразую в стандартный наш словарь и передам в data_base и logger
                data_base.add_deal(user_data)
                logger.logger(user_data, 'add') ## прошу написать функцию add в logger, которая принимает стандартный наш словарь и в данном случае признак add (добавить)
            
            case '5': # Изменить дело
                data = data_base.get_one_deal(deal_id)
                interface.show_deals(data)
                user_answer = interface.change_deal() ## user_answer - выбор юзера и/или измененные данные в удобном формате,
                                                      ## например {user_choise:1, deal_id: 11, User_input:'измененыый текст дела', deadline: 'not_changed', status: 1}
                                                      ## либо можем вообще убрать атрибут user_choise и передавать словарь с deal_id = -1, если новое дело, либо
                                                      ## укываем конкретный id и заменяем в базе полностью словарь с этим id
                
                change_action (user_answer) # функцию дописал в controller ниже, в которой формируем запрос для data_base.change
            
            case '6': # Выход
                interface.bye_mess() # прошу дописать функцию bye в interface (прощание с юзером)
                break
            
            case _:
                interface.error_input() # прошу дописать функцию error_input в interface, которая выведет сообщение что-то вроде "Введены некорректные данные"


def change_action(user_answer: dict):
    match user_answer['user_choise']:
        case 1: # завершить дело
            return
        
        case 2: # изменить дело
            return

        case 3: # удалить дело
            return
