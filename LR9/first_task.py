import random

with open("temperatures.txt", "w", encoding="utf-8") as file:
    for _ in range(15):
        temp = random.randint(-10, 35)
        file.write(f"{temp}\n")

print("Файл 'temperatures.txt' успішно створено та заповнено.")

total_sum = 0
positive_count = 0
total_count = 0

with open("temperatures.txt", "r", encoding="utf-8") as file:
    for line in file:
        temp = int(line.strip())
        total_sum += temp
        total_count += 1
        
        if temp > 0:
            positive_count += 1

average_temp = total_sum / total_count

print(f"\nСередня температура: {average_temp:.2f}°C")
print(f"Кількість додатних значень: {positive_count}")
