with open(r'file1.txt', 'r', encoding='utf-8') as file:
    data1 = file.readlines()

with open(r'file2.txt', 'r', encoding='utf-8') as file:
    data2 = file.readlines()

strokes1 = []
strokes2 = []

for i in range(len(data1)):
    data1[i] = data1[i].replace('\n', '')
for i in range(len(data2)):
    data2[i] = data2[i].replace('\n', '')

for i in data1:
    if i not in data2:
        strokes1.append(i)
for i in data2:
    if i not in data1:
        strokes2.append(i)

print(f"Несовпадающие строки в файле 1: \n {strokes1}")
print(f"Несовпадающие строки в файле 2: \n {strokes2}")
