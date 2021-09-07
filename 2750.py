n = int(input())

num_list = []
for i in range(n):
    a = int(input())
    num_list.append(a)


for j in range(1, len(num_list)):
    key = num_list[j]
    k = j - 1

    while k >= 0 and num_list[k] > key: #k > 0 으로 해서 첫 번째 거는 계속 제외해서 틀렸다가 프린트 해보고 앎
        num_list[k+1], num_list[k] = num_list[k], num_list[k+1]
        k -=1

for x in num_list:
    print(x)