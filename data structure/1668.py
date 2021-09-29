import sys

def ascending(_list):
    x = trophy_list[0]
    count = 1
    for j in range(1, len(_list)):
        if x < trophy_list[j]:
            count += 1
            x = trophy_list[j]
    return count


n = int(input())
trophy_list = []

for i in range(n):
    t = int(input())
    trophy_list.append(t)

print(ascending(trophy_list))
trophy_list.reverse()
print(ascending(trophy_list))