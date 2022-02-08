def solution(n):
    answer = map(int, list(str(n)))

    return sum(answer)
  
  # map을 list로 변환하지 않아도 바로 sum을 쓸 수 있음
  # 재귀함수를 이용해 풀 수 있다.
