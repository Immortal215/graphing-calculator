import random
import math
import os

def intCheck(inputString: str):
    if inputString[0] == "-":
        return inputString[1:].isdigit()
    else:
        return inputString.isdigit()
