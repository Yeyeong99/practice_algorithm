n = input().split()

for i in n:
    if n.count(i) == 1:
        answer = "yes"
    else:
        answer = "no"
        break

print(answer)