print('Добро пожаловать в домашний калькулятор(простой)')
first_number = input('Введите первое число: ')
good_first_number = first_number.isdigit()
while good_first_number == False:
          print('Не действительные данные.')
          first_number = input('Введите положительное число: ')
          good_first_number = first_number.isdigit()
first_number = int(first_number)

action = input('Выберите действие ("+", "-", "*", "/"): ')

second_number = input('Введите второе число: ')
good_second_number = second_number.isdigit()
while good_second_number == False:
          print('Не действительные данные.')
          second_number = input('Введите положительное число: ')
          good_second_number = second_number.isdigit()
second_number = int(second_number)
while (action == "*" or action == "/" and second_number == 0):
          print('!Запрещённое действие!')
          action = input('Выберите действие ("+", "-", "*", "/"): ')
          second_number = input('Enter second number: ')
          second_number = int(second_number)

print()

match action:
    case '+':
         print('Искомый ответ:', first_number + second_number)
    case '-':
         print('Искомый ответ:', first_number - second_number)
    case '*':
         print('Искомый ответ:', first_number * second_number)
    case '/':
         print('Искомый ответ:', int(first_number / second_number))
    case _:
         print('Не действительные данные. Попробуйте сначала.')