import datetime
def time(filename):
    date = datetime.datetime.now()
    dateNow = date.strftime('%a - %d/%b/%Y')
    timeNow = date.strftime('%H %M %S')
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(dateNow + " ")
        print()
        f.write(timeNow)