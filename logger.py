from datetime import datetime as dt


def logger(data, operation):
    time = dt.now()
    with open("log.txt", "a", encoding = 'utf8') as file:
        file.write(f"{data}; {operation}; {time} \n")
    return
