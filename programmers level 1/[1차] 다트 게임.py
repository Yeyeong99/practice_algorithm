import re
def solution(dartResult):
    scores = re.findall('\d*\D*', dartResult)
    scores.pop()
    result = []
    
    for score in scores:
        num = int(re.match('\d*', score).group())
        if 'D' in score:
            result.append(num ** 2)
        elif 'T' in score:
            result.append(num ** 3)
        else:
            result.append(num)
        if len(result) >= 2 :
            if '#' in score:
                result[-1] *= -1
            elif '*' in score:
                result[-1] *= 2
                result[-2] *= 2
        else:
            if '#' in score:
                result[-1] *= -1
            elif '*' in score:
                result[-1] *= 2 
        
    return sum(result)
  
  # p = re.compile('(\d+)([SDT])([*#]?)'
  # 위의 식을 이용하면 (숫자, 제곱수, *#)의 형식으로 넘겨받은 인자를 분리할 수 있다.
  # findall을 이용
