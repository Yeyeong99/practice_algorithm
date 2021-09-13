import sys

n = int(sys.stdin.readline().rstrip())

sorting = []
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    sorting.append(num)

for j in range(n):
    key = sorting[j]
    target_key = j - 1
    while target_key >= 0 and sorting[target_key] > key:
        sorting[target_key], sorting[target_key+1] = sorting[target_key+1], sorting[target_key]
        target_key -= 1 


for k in sorting:
    print(k)