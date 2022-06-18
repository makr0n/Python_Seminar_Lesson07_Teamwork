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
                status = interface.show_deals_by_status()
                while status not in range(1,6):
                    interface.error_input()
                    status = interface.show_deals_by_status()
                data = data_base.get_status_deal(status) ## прошу переименовать функцию get_data_undone в data_base
                interface.show_deals(data)
            
            
            case '3': # Добавить дело

                new_deal = interface.add_deal() # user_data - введенные юзером данные в удобном формате. Здесь я их преобразую в стандартный наш словарь и передам в data_base и logger
                data_base.add_deal(new_deal)
                logger.add(new_deal, 'add')
                interface.done_message()

            case '4': # Изменить дело
                data = data_base.get_all_deals()
                interface.show_deals(data)
                deal_id = interface.change_deal()
                one_deal = data_base.get_one_deal(deal_id)
                result = interface.change_deal_content(one_deal)
                if result['status'] == 10:
                    data_base.delete_deal(result['deal_id'])
                else:
                    data_base.change_deal(result)
            
            case '5': # Выход
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
