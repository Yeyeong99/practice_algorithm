# -*- coding: utf-8 -*-
"""백준_11399.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jBI7PoJfMRQYYDzPQoCts1EkEx9pQu48
"""

n = int(input())
p = list(map(int, input().split()))
p.sort()
result = 0

for i in range(1,len(p)+1):
  result += sum(p[:i])

print(result)

# 출처: https://deep-learning-study.tistory.com/629
n = int(input()) # 사람 수 
arr = list(map(int,input().split())) # 인출 시간
arr.sort() # 정렬

result = 0

for i in range(1,n):
    arr[i] += arr[i-1] # 인출 시간 갱신

print(sum(arr))