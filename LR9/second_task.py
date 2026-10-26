initial_data = [
    "2026-10-01;08:00;5\n",
    "2026-10-01;14:00;14\n",
    "2026-10-02;08:00;3\n",
    "2026-10-02;14:00;18\n",
    "2026-10-03;08:00;-2\n",
    "2026-10-03;14:00;11\n",
    "2026-10-04;08:00;7\n",
    "2026-10-04;14:00;22\n",
    "2026-10-05;08:00;4\n",
    "2026-10-05;14:00;16\n"
]

with open("weather_data.txt", "w", encoding="utf-8") as file:
    file.writelines(initial_data)

print("Файл 'weather_data.txt' створено з 10 записами.\n")


limit = float(input("Введіть граничне значення температури: "))

print(f"\nЗаписи з температурою вищою за {limit}:")
matching_count = 0


with open("weather_data.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        
       
        date, time, temp_str = line.split(";")
        temp = float(temp_str)

        if temp > limit:
            print(f"Дата: {date} | Час: {time} | Температура: {temp}°C")
            matching_count += 1

print(f"\nВсього знайдено записів: {matching_count}")
