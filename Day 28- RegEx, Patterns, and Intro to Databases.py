#!/bin/python3

import math
import os
import random
import re
import sys



    
if __name__ == '__main__':
    N = int(input().strip())
    list =[]
    for a0 in range(N):
        firstName,emailID = input().strip().split(' ')
        firstName,emailID = [str(firstName),str(emailID)]
        if re.search("@gmail.com",emailID):
            list.append(firstName)

print(*sorted(list), sep='\n')