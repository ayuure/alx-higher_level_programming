def read_file(filename=""):
    with open(filename, 'r') as f:
        f_content = f.read()
        print(f_content, end='')
