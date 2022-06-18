from datetime import datetime as dt

data = {'deal_id': 1, 'deal': 'Помыть кота', 'deadline': '12.05.2022', 'status': 'выполнено'}


def add(data, operation):
    time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding='utf8') as file:
        a = data['deal_id']
        b = data['deal']
        c = data['deadline']
        d = data['status']
        file.write(f"{a}) {b}. {c}. {d}. {operation}{time}")
    return


add(data, 'Изменено')
