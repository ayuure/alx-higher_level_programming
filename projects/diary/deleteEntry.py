import os
def delete():
    file_to_delete = input('Enter the name of the file you will like to delete')
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
    else:
        raise FileExistsError('file does not exist')
