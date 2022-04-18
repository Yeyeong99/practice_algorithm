n = int(input())
array = list(map(int, input().split()))

result = ['-1'] * n
for i in range(len(array)):
  for j in range(len(array[i:])):
    if array[i:][j] > array[i]:
      result[i] = str(array[i:][j])
      break
    elif array[i:][j] < array[i]:
      result[i] = '-1'
print(' '.join(result))
