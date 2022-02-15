def solution(s):
    answer = []
    for i in s:
        answer.append(i)
        if len(answer) >= 2:
            if answer[-2] == '(' and answer[-1] == ')':
                answer.pop(-1)
                answer.pop(-1)

    return len(answer) == 0
  
# '('일 땐 append 하고 ')'일 땐 answer에 '('가 있을 시 answer의 '('을 없애는 방법으로 구성할 수 있음
