# -*- coding: utf-8 -*-
"""prob_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JpvWH4zGWIWddr0nRQt5k_gZAkcN25OT
"""

def ispalindrome(s):
  return s == s[::-1]
s=str(input("enter any word :"))
ans= ispalindrome(s)
if ans :
  print("yes")
else:
  print("no")

def ispalindrome(s):
  return s == s[::-1]
s=str(input("enter any word :"))
ans= ispalindrome(s)
if ans :
  print("yes")
else:
  print("no")