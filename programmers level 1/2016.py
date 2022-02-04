def solution(a, b):
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    num = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    count = 0
    
    if a > 1:
        for i in range(a-1):
            count += num[i]
    count += b

    return days[count%7]
    
    # indexing과 sum을 활용하면 for을 쓰지 않아도 됨
