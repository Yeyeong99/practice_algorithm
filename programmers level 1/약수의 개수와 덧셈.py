def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        divid = 0
        for j in range(1, i+1):
            if i % j == 0:
                divid += 1
        if divid % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer 
  
  # 약수의 개수가 홀수 개인 숫자는 모두 제곱수라는 성질을 이용할 수 있다.
