# 시간 초과
n = int(input())
n_nums = list(map(int, input().split()))

m = int(input())
m_nums = list(map(int, input().split()))

def binary_search(array, num):
  array.sort()
  if len(array) == 0:
    return 0
  mid = len(array) // 2

  if array[mid] == num:
    return 1
  elif array[mid] > num:
    binary_search(array[:mid], num)
  else: 
    # mid+1 안할 경우 maximum recursion depth exceeded while calling a Python object
    binary_search(array[mid+1:], num)

for i in m_nums:
  binary_search(n_nums, i)

# 통과
n = int(input())
n_nums = list(map(int, input().split(' ')))
n_nums.sort()

m = int(input())
m_nums = list(map(int, input().split(' ')))

def binary(array, num, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == num:
            return 1
        elif array[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in m_nums:
    print(binary(n_nums, i, 0, n-1))
