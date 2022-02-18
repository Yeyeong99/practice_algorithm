# 재귀함수 이용하면 시간 초과

def solution(n):
    def fibo(n):
        if n <= 1:
            return n
        else:
            return fibo(n-1) + fibo(n-2)
    return fibo(n) % 1234567
  
# list 이용해서 풀어야함
def solution(n):
    answer = [0,1]
    for i in range(2, n+1): # 인덱스 상 두 번째부터 n번째까지 계산해야함
        answer.append((answer[i-1]+answer[i-2])%1234567)
    
    return answer[n]
