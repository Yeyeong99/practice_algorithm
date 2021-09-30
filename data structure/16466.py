import sys
n = int(input())

a = list(map(int, sys.stdin.readline().split()))

a.sort()

# enumerate 사용시: 중간에 빠진 제일 작은 값은 반환 외에 1,2,3 이런 식으로 연속으로 주어졌을 때 생각해야함
answer_list = []
for j in enumerate(a, start=1):
    if j[0] != j[1]:
        answer_list.append(j[0])
    else:
        if j[0] == len(a):
            answer_list.append(j[1]+1)

print(answer_list[0])