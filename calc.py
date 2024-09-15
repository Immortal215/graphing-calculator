import random
import math
import os
from functionsFile import *

white = (255, 255, 255)
black = (0, 0, 0)

# base arrays
operatorArray = ["+", "-", "*", "/"]
operatorList = []
numList = []

def calculate(inputArray):
    operatorList = []
    numList = []
    
    for i in inputArray:
        if intCheck(i):
            print("int")
            numList.append(int(i))
        else: 
            if i in operatorArray:
                print("\noperator\n")
                operatorList.append(i)
            else:
                print("Not an operator\n")
                calculate(input("Input numbers + operators : ").split())
        for i in range(0, len(inputArray), 2):
            if not intCheck(inputArray[i]):
                print("\nNot correct input notation\n")
                calculate(input("Input numbers + operators : ").split())

calculate(input("Input numbers + operators : ").split())
