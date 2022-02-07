from itertools import combinations

def solution(numbers):
    comb = list(combinations(numbers, 2))
    sum_list = list(set(list(map(lambda x:sum(x), comb))))
    sum_list.sort()
    return sum_list
  
# 이중 for 문을 이용해 모든 수를 더하고 set을 이용해 중복제거를 하는 방법도 있다.
