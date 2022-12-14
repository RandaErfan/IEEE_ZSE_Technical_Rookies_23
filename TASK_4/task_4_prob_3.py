# -*- coding: utf-8 -*-
"""task_4_prob_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LYqTDEYLcqHYyJ8a7-_4pveloMdu8TJq
"""

arr=[int(x) for x in input().split()]
def minimumDistance(arr):
	dic = dict()
	minDistance = 10**9
	prev_Index = 0
	curr_Index = 0
	for i in range(len(arr)):
		if arr[i] in dic:
			curr_Index = i
			prev_Index = dic[arr[i]]
			minDistance = min((curr_Index -
						prev_Index), minDistance)
		dic[arr[i]] = i
	if minDistance == 10**9:
		return -1
	return minDistance
minimumDistance(arr)