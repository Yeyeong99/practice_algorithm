# -*- coding: utf-8 -*-
"""백준_13305.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15bU0zj_qUfbKFnGwikkIvASM8RRbKcDd
"""

n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

answer = [prices[0]*distances[0]]

for i in range(1, n-1):
  answer.append(min(prices[i-1]*distances[i], prices[i]*distances[i]))

print(sum(answer))

min_ = prices[0]
sum = 0

for i in range(n-1):
  if min_ > prices[i]:
    min_ = prices[i]
  sum += (min_*distances[i])

print(sum)

