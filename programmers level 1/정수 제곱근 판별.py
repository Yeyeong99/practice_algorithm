def solution(n):
    return (n ** 0.5 + 1) ** 2 if n ** 0.5 - int(n ** 0.5) == 0 else -1

# float과 int를 빼지 않고 % 1로 나머지를 구하는 방법도 
