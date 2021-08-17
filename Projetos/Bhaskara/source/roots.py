from . import delt
from math import sqrt

def roots(a,b,c):
    numberDelt = delt.delt(a,b,c)
    print(numberDelt)
    if numberDelt < 0:
        return [0, 0, numberDelt]
    else:
        x1 = (-b + sqrt(numberDelt)) / 2*a
        x2 = (-b - sqrt(numberDelt)) / 2*a
        return [x1, x2, numberDelt]