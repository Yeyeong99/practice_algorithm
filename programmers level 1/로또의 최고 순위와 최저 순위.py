def solution(lottos, win_nums):

    highest = 0
    lowest = 0
    for i in lottos:
        if i in win_nums:
            highest += 1
            lowest += 1

    highest += lottos.count(0)

    if highest != 0:
        high_num = 7 - highest
    else: 
        high_num = 6

    if lowest != 0:
        low_num = 7 - lowest
    else: 
        low_num = 6
    return [high_num, low_num]

  # result = [0, 6, 5, 4, 3, 2, 1]를 설정할 때 0번째 자리를 6으로 설정했으면 더 간단하게 풀 수 있다. 
