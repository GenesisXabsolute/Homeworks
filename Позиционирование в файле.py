import io
from pprint import pprint


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf8')
    s = 0
    dict1 = dict()
    for i in strings:
        s += 1
        dict1[(s, file.tell())] = i
        file.write(i + '\n')
    return dict1


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
