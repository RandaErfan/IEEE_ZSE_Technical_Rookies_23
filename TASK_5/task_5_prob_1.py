# -*- coding: utf-8 -*-
"""TASK_5_prob_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z7ZCiffontEDXa1oQxALVxDy9UiZztmV
"""

def max_heapify(A,index):
    l = left(index)
    r = right(index)
    if l < len(A) and A[l] > A[index]:
        largest = l
    else:
        largest = index
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        max_heapify(A, largest)

def left(index):
    return 2 * index + 1

def right(index):
    return 2 * index + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for index in range(n, -1, -1):
        max_heapify(A,index)

A = [int(x) for x in input().split()]
build_max_heap(A)
print(" ")
print(A)