def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    for i in new_id:
        if i in list('~!@#$%^&*()=+[{]}:?,<>/'):
            new_id = new_id.replace(i, '')
    # 3
    # 주석 처리로 풀었다가 80점으로 테스트 통과 못함
    # an_new_id = new_id[0]
    # for i in range(1, len(new_id)):
    #     if new_id[i-1] != new_id[i]:
    #         an_new_id += new_id[i]
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # 4
    new_id = new_id.strip('.')
            
    # 5
    if len(new_id) == 0:
        new_id = 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    # 7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id
