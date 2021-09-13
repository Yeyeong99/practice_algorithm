#입력된 수의 인덱스의 값을 1씩 더해줌, 그리고 수가 바뀐 인덱스를 순서대로 1이 더해진 만큼 출력

import sys

n = int(sys.stdin.readline().rstrip())

sorting_array = [0] * 10001

for i in range(n):
    input_num = int(sys.stdin.readline())

    sorting_array[input_num] += 1

for i in range(len(sorting_array)):
    if sorting_array[i] != 0:
        for j in range(sorting_array[i]):
            print(i) #인덱스를 출력