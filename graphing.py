import random
import math

white = (255, 255, 255)
black = (0, 0, 0)

numArray = []
operatorArray = []

inputArray = input("Input numbers + operators : ").split()
for i in inputArray:
    try:
        # fix this stuff
       numArray.append(int(i))
        
    except TypeError:
        operatorArray.append(i)
