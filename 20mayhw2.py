import re

with open(r'file7.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

count_data_symbols = 0
vowels = []
consonants = []
digits = []
for i in data:
    count_data_symbols += len(i)
    digits += re.findall(r'[\d]', i)
    vowels += re.findall(r'[аеёиоуыюэя]', i, re.IGNORECASE)
    consonants += re.findall(r'[абвгджзйклмнпрстфхцчшщъь]', i, re.IGNORECASE)

count_data_digits = len(digits)
count_data_strokes = len(data)
count_data_vowels = len(vowels)
count_data_consonants = len(consonants)

with open(r'file3.txt', 'w', encoding='utf-8') as file:
    file.write(f'Количество символов - {count_data_symbols}\n')
    file.write(f'Количество строк - {count_data_strokes}\n')
    file.write(f'Количество гласных - {count_data_vowels}\n')
    file.write(f'Количество согласных - {count_data_consonants}\n')
    file.write(f'Количество цифр - {count_data_digits}')
