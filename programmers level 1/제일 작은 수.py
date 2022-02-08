def solution(arr):
    if len(arr) > 1:
        arr.pop(arr.index(min(arr)))
        return arr
    else:
        return [-1]
    
    # pop은 메모리 낭비일 수 있다.
    # list comprehension을 이용해서 작은 값보다 큰 값들로 새로운 list를 만들어 반환할 수 있다.
