def find_maximum_subarray(_list, low, high):
    if len(_list) == 1:
        return low, high, _list[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_max = find_maximum_subarray(_list, low, mid)
        right_low, right_high, right_max = find_maximum_subarray(_list, mid, high)
        cross_low, cross_high, cross_max = find_max_crossing_subarray(_list, low, mid, high)

        if (left_max > right_max and left_max > cross_max):
            return left_low, left_high, left_max
        elif (right_max > left_max and right_max > cross_max):
            return right_low, right_high, right_max
        else: 
            return cross_low, cross_high, cross_max

def find_max_crossing_subarray(_list, low, mid, high):
    left_sum = float('-inf')
    left_total = 0
    cross_low = mid

    for i in range(mid - 1, low - 1, -1):
        left_total = left_total + _list[i]
        if left_total > left_sum:
            left_sum = left_total
            cross_low = i

    right_sum = float('-inf')
    right_total = 0
    cross_high = mid + 1
    for j in range(mid, high):
        right_total = right_total + _list[j]
        if right_total > right_sum:
            right_sum = right_total
            cross_high = j
    return cross_low, cross_high, left_sum + right_sum





n = int(input())

num_list = []
for i in range(n):
    num_list.append(int(input()))

high, low, maximum = find_maximum_subarray(num_list, 0, len(num_list))

print(high)
print(low)
print(maximum)