
email = str(input("Введіть вашу пошту: "))

if "@" in email:
    domain = email.lower().split('@')[1]
    main = email.lower().split('@')[0]
    main = main.replace(main,"*" * len(main))
print(f'Ваш домен: {main}@{domain}')
