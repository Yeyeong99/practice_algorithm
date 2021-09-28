import sys

n = int(sys.stdin.readline())
pillow_list = []

for i in range(n):
    num = int(sys.stdin.readline())
    pillow_list.append(num)

answer = 0
start = 0

# # 이렇게 하면 중간에 같은 크기의 기둥이 나올 때 구분 못함
# for i in pillow_list:
#     if i > pillow_list[-1]:
#         answer += 1
#     else: 
#         continue

for i in range(1, n+1): 
    target = pillow_list[-i]
    if target > start:
        answer += 1
        start = target


print(answer)