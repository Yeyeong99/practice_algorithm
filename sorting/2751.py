# 시간 복잡도가 중요한 문제 - merge sort 이용해야함.

import sys

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j, k = 0, 0, 0 # 각각의 array에서의 요소를 각각 짚어야 하기 때문에.. 예를 들어 left의 두 번째와 right 의 첫 번째를 비교해야하는 경우가 있으니까

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            k += 1
            j += 1

    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            k += 1
            i += 1
    return array

n = int(sys.stdin.readline().rstrip())
sorting_array = []


for i in range(n):
    inputted_num = int(sys.stdin.readline().rstrip())
    sorting_array.append(inputted_num)

merge_sort(sorting_array)

for j in sorting_array:
    print(j)