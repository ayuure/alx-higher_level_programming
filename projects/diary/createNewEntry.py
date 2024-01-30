def entries(filename):
    text = input('What is on your mind today, Love🙂\n')
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text+'\n')