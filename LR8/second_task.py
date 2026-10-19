text = str(input("Введіть рядок: ")).lower()

try:
    index = int(input("Введіть індекс символу: "))
    char = text[index]
    
except ValueError as error:
    print(f'Помилка: введіть ціле число ({error})')
except IndexError as error:
    print(f'Помилка: вихід за межі рядка (такого індексу не існує) ({error})')
else:
    print(f"Символ у верхньому регістрі = {char.upper()}")
finally:
    print("Обробку запиту завершено.")
