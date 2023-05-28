def greetings():
    print ('Привет!')

def menu():
    print(
'''1 - Показать все контакты
2 - Добавить контакт
3 - Поиск
4 - Изменить контакт
5 - Удалить контакт
6 - Выход'''
)

def show_contacts(self):
    with open('file.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    print('\n')
    print (content)
    print('\n')


def success(self):
    print('\n')
    print ('Не удалось добавить контакт')
    print('\n')

def not_success(self):
    print('\n')
    print ('Контакт добавлен')
    print('\n')

def error():
    print('\n')
    print ('Ошибка ввода')
    print('\n')