total_sum = 0
count = 0

while True:
    number = int(input("Введіть ціле число (0 для завершення): "))
    
    if number == 0:
        break
        
    total_sum += number
    count += 1

if count > 0:
    average = total_sum / count
    print("Середнє арифметичне:", average)
else:
    print("Не було введено жодного числа перед 0.")