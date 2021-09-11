n, k = map(int, input().split())

num_list = [i for i in range(1, n+1)]
answer_list = []

a = k-1
while len(num_list):
    if a >= len(num_list):
        a -= len(num_list)
    else:
        answer_list.append(str(num_list.pop(a)))
        a += (k-1)

print("<",",".join(answer_list),">", sep="")