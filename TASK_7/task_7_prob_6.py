# -*- coding: utf-8 -*-
"""TASK_7_prob_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Z2Chw2xFTinUw1t-4D80F97ZdaRurv8
"""

import sys
def is_kaprekar(num):
    if num < 4:
        if num == 1:
            return True
        else:
            return False
    num_sq = pow(num, 2)
    num_sq_str = str(num_sq)
    
    left = num_sq_str[:len(num_sq_str)//2]
    right = num_sq_str[len(num_sq_str)//2:]
    
    #print("left = {} right = {}".format(left, right))
    
    if int(left) + int(right) == num:
        return True
    else:
        return False
    
def kaprekarNumbers(p, q):
    out = []
    for num in range(p, q + 1):
        if is_kaprekar(num):
            out.append(num)
    return out
p=int(input().strip())
q=int(input().strip())
result=kaprekarNumbers(p,q)
if result:
        print (" ".join(map(str, result)))
else:
        print("INVALID RANGE")