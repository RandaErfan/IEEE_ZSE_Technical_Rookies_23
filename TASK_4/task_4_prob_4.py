# -*- coding: utf-8 -*-
"""TASK_4_prob_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z7ZCiffontEDXa1oQxALVxDy9UiZztmV
"""

n=int(input())
digits=[int(x) for x in input().split()]
def AddOne(digits):
	index = len(digits) - 1
	while (index >= 0 and digits[index] == 9):
		digits[index] = 0
		index -= 1
	if (index < 0):
		digits.insert(0, 1)
	else:
		digits[index]+=1
AddOne(digits)
for digit in digits:
	print(digit, end =' ')