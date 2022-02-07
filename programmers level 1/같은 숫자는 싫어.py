def solution(arr):
    answer = [None]
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    return answer[1:]

  # answer[-1:]이면 빈문자열에서도 오류가 나지 않는다.
