import random

rng = random.Random()
dice_throw = rng.randrange(1, 7)

print(dice_throw)

delay_in_seconds = rng.random() * 5

print(delay_in_seconds)