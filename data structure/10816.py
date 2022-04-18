import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().split()))

answer = []

# 런타임 에러
for i in b:
    if i in a:
        c = str(a.count(i))
        answer.append(c)
    else:
        answer.append("0")

print(" ".join(answer))

# 시간 초과
for i in range(m):
  nums[i] = cards.count(answers[i])

print(*nums)

# 이진탐색 - 시간초과
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
answers = list(map(int, input().split()))

nums = [0] * m

cards.sort()
def binary(n, N, start, end):
  if start > end:
    return 0
  mid = (start+end)//2
  if n == N[mid]:
    return N[start:end+1].count(n)
  elif n < N[mid]:
    return binary(n, N, start, mid-1)
  else:
    return binary(n, N, mid+1, end)

for i in range(m):
  nums[i] = binary(answers[i], cards, 0, len(cards))

print(*nums)

# collections 활용 - 
from collections import Counter

c = dict(Counter(cards))
print(c)

for i in range(m):
  if answers[i] in c.keys():
    nums[i] = c[answers[i]]

print(*nums)
