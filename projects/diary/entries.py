delete = __import__('deleteEntry').delete
updatfFile = __import__('updateEntry').updatefile
time =  __import__('timeUpdates').time
entries = __import__('createNewEntry').entries
statements = __import__('statements').statements

def diary():
    statements()
    duty = input()
    while duty != 0:
        if duty == '1':
            filename = input('Enter a file name\n')
            text = input('What is on your mind today\n')
            entries(filename, text)
            time(filename)
        
        if duty == '2':
            filename = input('Enter name of file to update content\n')
            text = input("Enter text to add to file\n")
            updatfFile(filename, text)
        
        if duty == '3':
            file_to_delete = input('Enter the name of the file you will like to delete\n')
            delete(file_to_delete)
        
        if duty == '0':
            print('It was lovely having you here today')
        
        statements()
        duty = input()

diary()
