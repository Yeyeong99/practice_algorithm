def solution(numbers):
    num_tuple = tuple(range(10))
    answer = 0
    for i in num_tuple:
        if i not in numbers:
            answer += i
    return answer

  # 0-9의 합에서 numbers의 합을 빼면 간단하다..
