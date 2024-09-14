import random
import math

white = (255, 255, 255)
black = (0, 0, 0)

inputArray = input("Input numbers + operators : ").split()
for i in inputArray:
    try:
        # fix this stuff
        if isinstance(int(i), int):
            print("a")
        else: 
            print("b")
            
    except TypeError:
        break
