def solution(x):
    return True if x % sum(map(int, list(str(x)))) == 0 else False
  
  # if else 쓰지 않고 == 연산자만 써도 True False 판별 가능
