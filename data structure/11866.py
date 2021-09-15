n, k = map(int, input().split())
num_list = [i for i in range(1, n+1)]
answer = []

a = k-1
while len(num_list):
    if a < len(num_list):
        popped_num = num_list.pop(a)
        answer.append(str(popped_num))
        a += (k-1)
    else: 
        a -=len(num_list)


print("<",", ".join(answer),">", sep="")

