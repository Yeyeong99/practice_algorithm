def solution(s):
    if len(s) == 4 and s.isdecimal():
        answer = True
    elif len(s) == 6 and s.isdecimal():
        answer = True
    else:
        answer = False
    return answer
    
    # len(s) in (4, 6)으로 하면 조건을 두 가지로 나누지 않아도 됨
