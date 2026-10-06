users_numbers = list(map(int,input("Введіть 5 чисел ").split()))
new_tuple = tuple(users_numbers)
print(f"Ваш кортеж з 2 елементу по  4 включно: {new_tuple[1:4]}\n Ваш кортеж у зворотному порядку: {new_tuple[::-1]}")
