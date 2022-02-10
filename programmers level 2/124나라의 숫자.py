# 3의 배수가 아닐 땐 3진법으로 나타낸 수와 같다.
# 3의 배수인 경우엔 3으로 나누고 1을 뺀 값으로 업데이트 해준다.
# 효율성에서 점수 깎임
def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 0:
            answer += '4'
            n = n//3 -1
        else:
            answer += str(n%3)
            n //= 3
    return answer[::-1]
  
 # 통과
def solution(n):
    nums = [1, 2, 4]
    answer = ''
    while (n > 0):
        n -= 1
        answer = str(nums[n % 3]) + answer
        n = n // 3
    return answer
# 주어진 숫자에 1을 빼고 나머지를 구했을 때 나머지가 1일 땐 1, 2일 땐 2, 3일 땐 4가 나온다는 걸 이용해서 푸는 방법


# +) divmod와 재귀함수를 이용해 풀 수 있음
