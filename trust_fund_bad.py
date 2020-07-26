# Trus fund (bad edition)

print("""\t\tРантье
Программа суммирует все расходы (целочисленные)
Вводите всё по порядку.\n
""")

car = input("Машина: ")
rent = input("Квартира: ")
jet = input("Самолёт: ")
gifts = input("Подарки: ")
food = input("Обеды: ")
staff = input("Домработники: ")
guru = input("Психоаналитик: ")
games = input("Игры: ")
total = car + rent + jet + gifts + food + staff + guru + games

print("Общая сумма:", total, "₽")
