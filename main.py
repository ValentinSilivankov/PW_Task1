from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

text = '''Список комманд:
1 - вызов функции calculate_salary
2 - вызов функции get_employees
e - выход из программы
'''

if __name__ == '__main__':
    print(f'Здравствуйте!\nСегодня {datetime.today()}')
      
    while True:
        print(text)
        search = str(input('Введите комманду: '))
        if search == '1':
            calculate_salary()
        elif search == '2':
            get_employees()
        elif search == 'e':
            break
        else:
            print('Нет такой комманды!!!')   