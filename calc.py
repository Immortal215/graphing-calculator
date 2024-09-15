import random
import math
import os
from functionsFile import *

white = (255, 255, 255)
black = (0, 0, 0)

inputArray = input("Input numbers + operators : ").split()

for i in inputArray:
    try:
        if intCheck(i):
            print("a")
        else: 
            print("b")
            
    except TypeError:
        break
    
    
