# Craps roller

import random

die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1
total = die1 + die2

print(f"{die1 = }, {die2 = }, {total = }")
