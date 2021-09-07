n, k = map(int, input().split())

num_list = [i for i in range(1, n+1)]
answer_list = []

a = k-1
while len(num_list) != 0:
    n_list = num_list[:a]
    answer_list.append(num_list[a])
    del num_list[a]
    a += len(n_list)
    if a > len(num_list):
        a -= 

    print(answer_list)