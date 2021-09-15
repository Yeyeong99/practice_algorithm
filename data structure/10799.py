n = list(input())
s= []
answer = 0

for i in range(len(n)):
    if n[i] == '(':
        s.append('(')
    else:
        if n[i-1] == '(': #레이저인 경우
            s.pop()
            answer += len(s)
        else: 
            s.pop()
            answer +=1


print(answer)
