def solution(numbers):
    numbers = list(map(str, numbers))
    #numbers의 원소가 1000 이하이기 때문에 세 자리수로 맞춘 후 비교하겠다는 의미
    # 앞 자리 숫자부터 큰 순서로 차례로 배열해줌
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 모든 값이 0인 경우를 처리하기 위해 int로 변환한 후 str로 변환(ex 000 -> 0)
    return str(int(''.join(numbers)))

# 순열조합을 이용하는 경우 시간 초과
