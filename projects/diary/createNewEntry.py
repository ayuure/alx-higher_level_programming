def entries(filename, text):
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text+'\n')