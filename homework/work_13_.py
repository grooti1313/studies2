number_of_tickets = int(input("Введите количество билетов: "))
visitor_age = int(input("Введите ваш возраст: "))

if visitor_age < 18:
    amount = 0
elif visitor_age >= 18 and visitor_age < 25:
    amount = 990
else:
    amount = 1390

if number_of_tickets > 3:
    discount = amount * 0.01
    amount = amount - discount

print(amount, "руб.")