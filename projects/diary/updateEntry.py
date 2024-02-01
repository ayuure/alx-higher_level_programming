import datetime
import os
def updatefile(filename, text):
    date =  datetime.datetime.now()
    update_date = date.strftime('%a - %d/%b/%Y')
    if os.path.exists(filename):
        with open(filename, mode='a', encoding='utf-8') as f:
            f.write('\n' + text)
            f.write(' - Updated on: ' + update_date)
    else:
        raise FileExistsError('file does not exist')