# -*- coding: utf-8 -*-
"""TASK_7_prob_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Z2Chw2xFTinUw1t-4D80F97ZdaRurv8
"""

#if __name__ == '__main__':
alist = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))