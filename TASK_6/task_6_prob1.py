# -*- coding: utf-8 -*-
"""TASK_6_prob1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z7ZCiffontEDXa1oQxALVxDy9UiZztmV
"""

num=int(input())
digits= [int(x) for x in str(num)]
temp = num
if (temp > 9):
  total=0
  for j in range(len(str(num))):
      if digits[j]%10 ==0:
        continue
      elif digits[j]%10 != 0 and temp%(digits[j]%10)==0:
          total += 1
          num /= 1
  print(total)