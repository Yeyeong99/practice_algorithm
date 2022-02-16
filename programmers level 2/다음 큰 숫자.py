def solution(n):
    def digit(k):
        num = ''
        while k > 0:
            num += str(k%2)
            k //= 2
        return num[::-1]
    for i in range(n+1, 1000001):
        if digit(i).count('1') == digit(n).count('1'):
            return i
          
          
# bin이라는 함수가 있었다..
# while을 이용해서 n 초과부터 1씩 증가시키며 비교하는 방법도 있다.
