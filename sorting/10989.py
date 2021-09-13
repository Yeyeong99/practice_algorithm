import sys

n = int(sys.stdin.readline().rstrip())

sorting_array = []
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    sorting_array.append(num)

for j in range(len(sorting_array)):
    key = sorting_array[j]
    target_key = j - 1
    while target_key >= 0 and key < sorting_array[target_key]:
        sorting_array[target_key], sorting_array[target_key+1] = sorting_array[target_key+1], sorting_array[target_key]
        target_key -=1

for k in sorting_array:
    print(k)