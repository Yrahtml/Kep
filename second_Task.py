x = float(input("x = "))
y = float(input("y = "))

if x == 0 or y == 0:
    print("Точка лежить на осі координат")
elif x > 0 and y > 0:
    print("I чверть")
elif x < 0 and y > 0:
    print("II чверть")
elif x < 0 and y < 0:
    print("III чверть")
else:
    print("IV чверть")