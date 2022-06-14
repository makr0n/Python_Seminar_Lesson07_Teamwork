import json

data = [{'deal_id':1, 'deal':'Помыть кота', 'deadline': '12.05.2022', 'status':1}, {'deal_id':2, 'deal':'Постирать', 'deadline': '12.07.2022', 'status':0}]

def change (deal, deal_id = -1):
    with open ('db.json', 'r') as file:
        data = json.load(file) #тип data должен быть list
        if len(data)<2:
            return 'baseIsEmpty'
    if deal_id == -1:
        data.append(deal)
    else:
        -1 # внести в указанное дело изменения

def get_data_undone ():
    with open ('db.json', 'r') as file:
        data = json.load(file) #тип data должен быть list
        if len(data)<2:
            return 'baseIsEmpty'
    return [deal for deal in data if deal['status'] == 0]

    
def clear_db ():
    first_element = ({'id_counter' : 0},{'deal_id':1, 'deal':'Помыть кота', 'deadline': '12.05.2022', 'status':1}, {'deal_id':2, 'deal':'Постирать', 'deadline': '12.07.2022', 'status':0})
    with open ('db.json', 'w') as file:
        json.dump(first_element, file)

if __name__ == "__main__":
    clear_db ()

