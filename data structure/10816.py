import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().split()))

answer = []

for i in b:
    if i in a:
        c = str(a.count(i))
        answer.append(c)
    else:
        answer.append("0")

print(" ".join(answer))