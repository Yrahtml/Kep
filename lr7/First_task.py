BOOK = {
    "Кобзар": 1,
    "1984" : 4,
    "Тигролови" :2
}

BOOK["Захар Беркут"] = 3

BOOK["1984"] -= 1
BOOK['Захар Беркут'] -=1
print("Повний список книг та їх кількість")
for title, count in BOOK.items():
    print(f"'{title}': {count} шт.")

print("\nКниги, яких залишилося менше 3 примірників")
for title, count in BOOK.items():
    if count < 3:
        print(f"'{title}': {count} шт.")
