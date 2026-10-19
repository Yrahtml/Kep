try:
    all = int(input("Введіть кількість завдань: "))

    completed = int(input("Введіть кількість виконаних завдань: "))
    
    if all > 0 and completed <= all:

        percent = (completed / all) * 100
        
        print(f'Частка виконаних завдань = {percent:.0f}%')
    else:
        print("Помилка: перевірте коректність введених даних (загальна кількість має бути > 0, а виконаних — не більше за загальну).")

except ZeroDivisionError as error:
    print(f'Помилка {error}')
except ValueError:
    print('Помилка: потрібно вводити числа!')
