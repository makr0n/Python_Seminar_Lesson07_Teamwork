from datetime import datetime as dt

dict = {1: 'Новое', 2: 'В работе', 3: "Отложенное", 4: "Просроченное", 5: "Выполненное"}


def add(data, operation):
    time = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a", encoding='utf8') as file:
        a = data['deal_id']
        b = data['deal']
        c = data['deadline']
        d = data['status']
        if d != 10:
            file.write(f"{a}) {b}. {c}. {dict[d]}. |{operation} {time}|\n")
        else:
            file.write(f"{a}) {b}. {c}. |{operation}' '{time}|\n")
    return
