from itertools import combinations

def solution(nums):
    answer = 0
    comb = list(combinations(nums, 3))
    sum_list = [sum(i) for i in comb]
    for i in sum_list:
        i_num = []
        for j in range(1, i+1):
            if i % j == 0:
                i_num.append(0)
        if len(i_num) == 2:
            answer += 1
    return answer
  
  # itertools combination 기억하기, 사용할 경우 list로 변환해야함
