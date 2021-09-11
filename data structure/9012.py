t = int(input())

for i in range(t):
    count = 0
    answer = list(input())
    for j in range(len(answer)):
        if answer[j] == "(":
            count += 1
        elif answer[j] == ")":
            count -= 1
        
        if count < 0: 
            print("NO")
            break
    if count > 0:
        print("NO")
    elif count == 0:
        print("YES")
