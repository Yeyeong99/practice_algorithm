def solution(n):
    result = ''
    while n >= 1:
        result += str(n % 3)
        n = n // 3
    
    answer = 0
    for idx, i in enumerate(reversed(result)):
        answer += int(i)*(3**(idx))
    
    return answer

# int(num, n) => n진법으로 쓰인 숫자를 10진법으로 변환해줌
