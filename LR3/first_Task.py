def check_three_numbers(a, b, c):
    numbers = [a, b, c]
    max_num = max(numbers)
    count = numbers.count(max_num)
    return max_num, count

def max_in_range(a, b, step):
    sequence = list(range(a, b + 1, step))
    return max(sequence)

print("Введіть 3 числа які хочете порівняти")
a=int(input("a = "))
b=int(input("b = "))
c =int(input("c = "))

num_max, num_count = check_three_numbers(a, b, c)
print(f"Найбільше число: {num_max}, повторюється разів: {num_count}")

seq_max = max_in_range(a, b, c)
print(f"Найбільше значення в послідовності: {seq_max}")
