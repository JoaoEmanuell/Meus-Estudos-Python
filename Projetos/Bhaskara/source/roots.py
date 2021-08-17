from delt import delt
from math import sqrt

def roots(a,b,delt):
    if delt < 0:
        return [0, 0, delt]
    else:
        x1 = (-b + sqrt(delt)) / 2*a
        x2 = (-b - sqrt(delt)) / 2*a
        return [x1, x2, delt]

