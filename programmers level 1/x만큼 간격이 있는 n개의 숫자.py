# 1 개 런타임 에러
def solution(x, n):
    if x >= 0:
        return list(range(x, n*x+1, x))
    else:
        answer = list(range(n*x, x+1, -x))
        answer.reverse()
        return answer

# 통과
def solution(x, n):
    return [x * i for i in range(1, n+1)]
