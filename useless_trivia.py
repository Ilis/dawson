# Useless trivia

name = input("Hi! What's your name? ")
age = input("How old are you? ")
age = int(age)
weight = int(input("What is your weight? "))

print()
print("If Cammings write you a letter, he write", name.lower())
print("If mad Cammings write you a letter, he write", name.upper())

called = name * 5
print("Kid can call you like this:", called)

seconds = age * 365 * 24 * 60 * 60
print("Your age in seconds is:", seconds)

moon_weight = weight / 6
print("Your weight on the Moon is:", moon_weight)

sun_weight = weight * 27.1
print("Your weight on the Sun is:", sun_weight)
