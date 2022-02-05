def solution(array, commands):
    answer = []
    for command in commands:
        new_array = array[command[0]-1:command[1]]
        new_array.sort()
        answer.append(new_array[command[2]-1])
    return answer

# list.sort()는 할당하지 않는다.
# j,k,y = command 이런 식으로 할당하면 가독성이 올라간다.
# lambda를 이용하면 한 줄로 풀 수 있다.
