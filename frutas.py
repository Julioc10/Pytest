from random import randint

frutas = randint(1, 3)

def fruta():
    if frutas == 1:
        return 'banana'
    if frutas == 2:
        return 'manga'
    if frutas == 3:
        return 'goiaba'

print(frutas)
