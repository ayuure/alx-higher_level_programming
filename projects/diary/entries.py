delete = __import__('deleteEntry').delete
updatfFile = __import__('updateEntry').updatefile
time =  __import__('timeUpdates').time
entries = __import__('createNewEntry').entries

def diary():
    duty =  '1'
    while duty !='0':
        print('Hi and welcome to your personal diary. Feel free to enter all your thoughts')
        print('Enter 1 to create a new file')
        print('Enter 2 to update an exisiting file')
        print('Enter 3 to delete an exisiting file')
        print('Enter 0 to exit')
        duty = input()
        if duty not in ['0','1','2','3']:
            raise TypeError('Wrong Input. Acceptable inputs are 0, 1, 2, 3')

        
    

try:
    diary()
except TypeError as e:
    print(e)
