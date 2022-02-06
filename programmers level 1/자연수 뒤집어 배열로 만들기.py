def solution(n):
    answer = list(map(int, reversed(list(str(n)))))
    return answer
 
# list 변환 없이 바로 reversed 사용 가능
