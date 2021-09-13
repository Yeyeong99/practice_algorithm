import sys

n = int(sys.stdin.readline().rstrip())

num_list = []

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    num_list.append(num)

for j in range(len(num_list)):
    key = num_list[j]
    target_key = j - 1
    while target_key >= 0 and num_list[target_key] > key: #target_key가 0부터 시작해야 [0]부터 적용됨
        num_list[target_key], num_list[target_key+1] = num_list[target_key+1], num_list[target_key]
        target_key -= 1

for k in num_list:
    print(k)