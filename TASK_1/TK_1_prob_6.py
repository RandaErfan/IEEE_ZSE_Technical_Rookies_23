# -*- coding: utf-8 -*-
"""prob_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZWbj8ymEjmQHi-ifY_CRR2MpYoCSDBJH
"""

#6
a=int(input())
b=int(input())
def gcd(a, b):
	if (a == 0):
		return b
	if (b == 0):
		return a
	if (a == b):
		return a
	if (a > b):
		return gcd(a-b, b)
	return gcd(a, b-a)
gcd(a,b)