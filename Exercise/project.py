from random import random as rand
from math import floor

lowlimit = int(input('Enter the lower bound: '))
highlimit = int(input('Enter the upper bound: '))

rangelimit = highlimit - lowlimit + 1
picknumber = floor(rand() * rangelimit) + lowlimit

print(picknumber)