# -*- coding: utf-8 -*-
"""prob_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z7ZCiffontEDXa1oQxALVxDy9UiZztmV
"""

#3
n=int(input("the length of array : "))
l=[]
for i in range(0,n):
  x=int(input())
  l.append(x)
print(l)
def forloop(l,n):
  sum=0
  for i in range(0,n):
    sum+=l[i]
  print(sum)
forloop(l,n)
def whileloop(l,n):
  sum=0
  i=0
  while i<n :
    sum+=l[i]
    i+=1
  print(sum)
whileloop(l,n)

def recrusion(l,n):
  if n<=0 :
     return 0
  else : 
    return(recrusion(l,n-1)+l[n-1])
recrusion(l,n)