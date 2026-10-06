numbers = list(map(int, input("Введіть числа через пропуск: ").split()))

average = sum(numbers) / len(numbers)
bigger = []
for i in range(len(numbers)):
    if numbers[i] > average:
        bigger.append(numbers[i])
        i+1 
print(f"Середнє значення вашого списку {average}\n Числа що більші за середнє значення {bigger}")
