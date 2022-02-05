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
#========================================================#
# 통과
def solution(numbers, hand):
    # 리스트로 할당하지 않고 빈문자열로 할당해서 더해주는 방식도 있음
    answer = []
    point = [(3,1), (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2), (3,0), (3,2)]
    r_hand = point[-1]
    l_hand = point[-2]
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer.append('L')
            l_hand = point[i]
        elif i == 3 or i == 6 or i == 9:
            answer.append('R')
            r_hand = point[i]
        else:
            # 차를 제곱하고 더해서 루트 씌우는 식으로 계산하면 안된다. 대각선인 경우 이동하지 못하기 때문에 아래와 같은 방식으로 계산해줘야함
            r_distance = abs(r_hand[0]-point[i][0]) + abs(r_hand[1]-point[i][1])
            l_distance = abs(l_hand[0]-point[i][0]) + abs(l_hand[1]-point[i][1])
            if r_distance > l_distance:
                answer.append('L')
                l_hand = point[i]   
            elif r_distance < l_distance:
                answer.append('R')
                r_hand = point[i]
            else:
                if hand == 'right':
                    answer.append('R')
                    r_hand = point[i]
                else:
                    answer.append('L')
                    l_hand = point[i]
                    
                
    return ''.join(answer)
