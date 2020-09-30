#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    length = len(arr)
    possitiveNum = 0 
    negetiveNum = 0
    zeroNum = 0
    possitiveRatio = 0
    negetiveRatio = 0
    zeroRatio = 0
    for i in range(length):
        if (arr[i] < 0 ):
            negetiveNum += 1
        elif (arr[i]>0):
            possitiveNum += 1
        else:
            zeroNum += 1

    possitiveRatio = possitiveNum/length
    negetiveRatio = negetiveNum/length
    zeroRatio = zeroNum/length

    print(round(possitiveRatio,6))
    print(round(negetiveRatio,6))
    print(round(zeroRatio,6))
    


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
