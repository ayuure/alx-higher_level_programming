import datetime
def entries(filename):
    names = []
    filename = input('Enter filename\n')
    for _ in names:
        if _ == filename:
            raise FileExistsError('Filename already exist, will you like to replace file?')
    date = datetime.datetime.now()
    dateNow =  date.strftime('%a - %d / %b / %Y')
    time = date.strftime('%H, %M, %S')
    text = input('What is on your mind today\n')
    print(dateNow)
    print(time)
    with open(filename, mode='w', encoding='utf-8' ) as f:
        f.write(text)

entries('file')