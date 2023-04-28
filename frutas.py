from random import randint

frutas = randint(1, 5)

def fruta():
    if frutas == 1:
        return 'banana'
    if frutas == 2:
        return 'maca'
    if frutas == 3:
        return 'pera'
    if frutas == 4:
        return 'mamao'
    if frutas == 5:
        return 'manga'

print(frutas)
