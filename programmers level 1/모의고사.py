def solution(answers):
    pick = {1: [1, 2, 3, 4, 5] * 2000,
            2: [2, 1, 2, 3, 2, 4, 2, 5] * 1250,
            3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000}
    answer = {1: 0, 2: 0, 3: 0}
    
    for k in range(1, 4):
        for i, j in zip(answers, pick[k]):
            if i == j:
                if k == 1:
                    answer[1] += 1
                elif k == 2:
                    answer[2] += 1
                else:
                    answer[3] += 1
    max_num = max(answer[1], answer[2], answer[3])
    result = [i for i, j in answer.items() if j == max_num]
    result.sort()
    return result
  
  # for 에서 enumerate를 이용해 answers 만 사용하고(이렇게 하면 range(len()) 이런 식으로 하지 않아도 됨), idx 같은 경우 %를 이용해 구할 수 있다.
