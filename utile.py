from math import sqrt
from random import uniform

def Distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def sommeDistances(points):
    s = 0
    for i in range(len(points)):
        dist = Distance(points[i], points[(i+1) % len(points)])
        s += dist
    return s

def selectionnerParent(list, probabilities):
    index = 0
    r = uniform(0,1)
    while r > 0:
        r = r - probabilities[index]
        index += 1
    index -= 1
    return list[index].copy()

