
_list = [3, -1, 6, -5, -10]
mid = len(_list) // 2
left = _list[:mid]
right = _list[mid:]

left_sum = float('-inf')
left_total = 0
cross_mid = len(_list) // 2
cross_left = _list[:cross_mid]

for i in range(len(cross_left)-1, -1, -1):
    print(f"i: {i}")
    left_total = left_total + cross_left[i]
    if left_total > left_sum:
        left_sum = left_total
        max_left = i

print(left, right)