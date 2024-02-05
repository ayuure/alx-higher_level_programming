import os
def readFile(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        if os.path.exists(filename):
            print(f.read())
        else:
            raise FileExistsError('file does not exist')