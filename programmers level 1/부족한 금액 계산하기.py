def solution(price, money, count):
    answer = list(map(lambda x: x*price, list(range(1, count+1))))
        
    return sum(answer) - money if sum(answer) - money > 0 else 0
  
  
# return 부분은 max를 이용해 나타낼 수 있다. 
