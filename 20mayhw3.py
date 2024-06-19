with open(r'file4.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
    data.pop(-1)
    print(data)

with open(r'file5.txt', 'w', encoding='utf-8') as file:
    for i in data:
        file.write(i)
