def find_max_crossing_subarray(cross_list):
    left_sum = float('-inf')
    left_total = 0
    cross_mid = len(cross_list) // 2
    
    for i in range(cross_mid - 1, -1, -1):
        left_total = left_total + cross_list[i]
        if left_total > left_sum:
            left_sum = left_total
            max_left = i

    right_sum = float('-inf')
    right_total = 0
    cross_right = cross_list[cross_mid:]
    for j in range(len(cross_right)):
        right_total = right_total + cross_list[j]
        if right_total > right_sum:
            right_sum = right_total
            max_right = j + 1
    return [max_left, max_right, left_sum + right_sum]



def find_maximum_subarray(_list):
    if len(_list) == 1:
        return [0,0,_list[0]]
    else:
        mid = len(_list) // 2
        left = find_maximum_subarray(_list[:mid])
        right = find_maximum_subarray(_list[mid:])
        cross = find_max_crossing_subarray(_list)

        if left[2] >= right[2] and left[2] >= cross[2]:
            return left
        elif right[2] >= left[2] and right[2] >= cross[2]:
            return right
        else: 
            return cross


n = int(input())

num_list = []
for i in range(n):
    num_list.append(int(input()))

result = find_maximum_subarray(num_list)

for i in result:
    print(i)