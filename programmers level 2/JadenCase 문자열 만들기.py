# split에서 ' '로 해줘야함. 공백이 연속으로 나올 수 있다고 했기 때문
# 마지막에 ' '로 이어주기 때문에 여러 개의 공백이 있는 상태를 반영하지 못함.

def solution(s):
    s_list = s.split(' ')
    
    for idx, i in enumerate(s_list):
        s_list[idx] = s_list[idx].capitalize()
            
    return ' '.join(s_list)
  
  
# title을 이용하면 통과 못함
# 아무래도 한 번 변환한 뒤 다시 확인하며 변환하는 과정을 거쳐서 그런듯?
def solution(s):
    s = s.title()
    s_list = s.split()
    
    for i in s_list:
        if i[0].isdigit():
            s_list[s.index(i)] = i.lower()
            
    return ' '.join(s_list)
