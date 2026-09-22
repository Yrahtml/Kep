n = int(input("Введіть число: "))

def calculation(n):
    if n <= 0:
        return 0
    return n*n + calculation(n-1)

print(f"Сума квадратів чила {n}  {calculation(n)}")

