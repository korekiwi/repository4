with open (r'file6.txt', 'r', encoding='utf-8') as file:
    search_word = input("Введите искомое слово: ")
    data = file.readlines()
    count = 0
    for i in data:
        count += i.count(search_word)
    print(count)