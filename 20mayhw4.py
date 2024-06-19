with open (r'file4.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    max_len = 0
    for i in data:
        if len(i) > max_len:
            max_len = len(i)
    print(max_len)