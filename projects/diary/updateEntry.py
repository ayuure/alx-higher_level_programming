import datetime
def updatefile(filename):
    date =  datetime.datetime.now()
    update_date = date.strftime('%a - %d/%b/%Y')
    text = input('Enter update\n')
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(text +'/n')
        f.writ(update_date)