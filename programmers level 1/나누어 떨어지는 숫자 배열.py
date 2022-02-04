def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    answer.sort()
    if len(answer) == 0:
        answer = [-1]
    return answer
    
    # return 에서 or 연산자를 사용할 수 있음. 리스트가 비어있으면 False라서 or 뒤에 있는 값을 반환함
