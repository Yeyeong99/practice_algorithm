import sys

n = int(sys.stdin.readline().rstrip())

sorting_list = []
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    sorting_list.append(num)

for j in range(len(sorting_list)):
    key = sorting_list[j]
    target_key = j - 1
    while target_key >= 0 and sorting_list[target_key] > key:
        sorting_list[target_key+1], sorting_list[target_key] = sorting_list[target_key], sorting_list[target_key+1]
        target_key -= 1

for i in sorting_list:
    print(i)
