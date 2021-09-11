n = int(input())

num_list = []
op = []
temp = True
count = 1
for i in range(n):
    k = int(input())
    while count <= k:
        num_list.append(count)
        op.append('+')
    if num_list[-1] == k:
        num_list.pop()
        op.append('-')
    else:
        temp = False

if temp == False:
    print('No')
else:
    for i in op:
        print(i)


