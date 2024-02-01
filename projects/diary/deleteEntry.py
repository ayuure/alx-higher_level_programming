import os
def delete(file_to_delete):
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
    else:
        raise FileExistsError('file does not exist')