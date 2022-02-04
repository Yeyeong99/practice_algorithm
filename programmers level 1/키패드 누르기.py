def solution(numbers, hand):
    answer = []
    r_hand = 0
    l_hand = 0
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer.append('L')
            l_hand = i
        elif i == 3 or i == 6 or i == 9:
            answer.append('R')
            r_hand = i
        else:
            if abs(r_hand-i) == abs(l_hand-i) or abs(abs(r_hand-i)-abs(l_hand-i)) == 2:
                if hand == 'right':
                    answer.append('R')
                else: 
                    answer.append('L')
            elif abs(r_hand-i) < abs(l_hand-i):
                answer.append('R')
            else:
                answer.append('L')
                
    return ''.join(answer)
  
# 2와 5, 4와 5의 거리 차이 구분 못함.
