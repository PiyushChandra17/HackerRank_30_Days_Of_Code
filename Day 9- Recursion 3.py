#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
factorial = lambda x: 1 if x<=1 else x * factorial(x-1)

print(factorial(int(input())))

if __name__ == '__main__':
    

    x = int(input())
