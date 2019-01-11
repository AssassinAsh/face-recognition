# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 14:56:58 2018

@author: ashvin
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    count1 =count2 = count3 = count4 = count5 = 0
    list1 = []
    for i in range(0,len(arr)):
        if arr[i] == 1:
            count1 += 1
        if arr[i] == 2:
            count2 += 1
        if arr[i]==3:
            count3 += 1
        if arr[i] ==4:
            count4 += 1
        if arr[i] ==5:
            count5 +=1
    list1.append(count1)
    list1.append(count2)
    list1.append(count3)
    list1.append(count4)
    list1.append(count5)
    print(list1)
    return list1.index(max(list1)) + 1
                        
if __name__ == '__main__':
   

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')

