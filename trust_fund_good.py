# Trus fund (not bad edition)

print("""\t\tРантье
Программа суммирует все расходы (целочисленные)
Вводите всё по порядку.\n
""")

car = int(input("Машина: "))
rent = int(input("Квартира: "))
jet = int(input("Самолёт: "))
gifts = int(input("Подарки: "))
food = int(input("Обеды: "))
staff = int(input("Домработники: "))
guru = int(input("Психоаналитик: "))
games = int(input("Игры: "))
total = car + rent + jet + gifts + food + staff + guru + games

print("Общая сумма:", total, "₽")
