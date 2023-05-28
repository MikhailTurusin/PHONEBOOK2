def get_data():
    with open('file.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    return data

def add_contact(contact):
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write('\n')
        file.write(contact)

def change (result):
    with open('file.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
    with open('file.txt', 'w', encoding='utf-8') as file:
        for line in content:
            if line.strip('\n') != result:
                file.write(line)
        file.write('\n')
        file.write(input('Введите новые данные: '))
    print('\n')
    print (f'Данные контакта {result} изменены')
    print('\n')