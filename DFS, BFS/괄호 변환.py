# https://programmers.co.kr/learn/courses/30/lessons/60058
def solution(p):
    def split_uv(p):
        _list = []
        _list.append(p[0])
        # u를 분리하기 위한 과정
        for idx in range(1, len(p)):
            _list.append(p[idx])
            if _list.count('(') == _list.count(')'):
                u = ''.join(_list)
                break
        # v
        p_list = [i for i in p]
        for idx in range(len(u)):
            if u[idx] == p_list[idx]:
                p_list[idx] = ''

        v = ''.join(p_list)
        
        return u, v
    def right(string):
        _list = []
        _list.append(string[0])
        for idx in range(1, len(string)):
            _list.append(string[idx])
            if _list[0] == '(' and _list.count('(') == _list.count(')'):
                return True
        return False      
    
    if right(p):
        return p
    else:
        u, v = split_uv(p)
    
    answer = ''
    return answer
