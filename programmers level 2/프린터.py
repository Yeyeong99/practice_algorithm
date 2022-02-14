def solution(priorities, location):
    answer = 0
    m = max(priorities)
    while True:
        v = priorities.pop(0)
        if m == v:
            answer += 1 # 한 번 프린트 한 것으로 취급
            if location == 0:
                break # 가장 큰 값과 같을 경우에 우선순위가 가장 첫 번째인 경우이므로, 한 번 프린트 되면 끝나는 것
            else:
                # 맨 앞 값이 출력되어 사라지니 location도 하나 작아짐
                # 뒤에 값이 append 되어 index 값이 앞으로 당겨지는 것과는 다름
                location -= 1 
            # 이 if 문 안에선 이미 max 값이 출력됨.
            # 따라서 max 값을 새롭게 업데이트
            m = max(priorities)
        else:
            priorities.append(v)
            if location == 0:
                # append 되고 달라지는 순서를 반영
                # 맨 끝자리에 append 되니 길이-1
                location = len(priorities) - 1
            else:
                # 다른 값이 추가될 경우 앞으로 한 칸 이동
                location -= 1
    return answer
