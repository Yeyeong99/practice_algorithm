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

# 통과
# 스택을 이용해서 인덱스 저장
n = int(input())
array = list(map(int, input().split()))

result = ['-1'] * n
stack = [0] # index 저장하는 용도

for i in range(1, n):
  while stack and array[stack[-1]] < array[i]:
    result[stack.pop()] = array[i]
  stack.append(i) # 5 4와 같은 경우는 while문을 수행하지 않고 바로 이 줄을 시행함. 그리고 다음 수행에서 pop으로 마지막에 들어간 인덱스를 꺼내줌.

print(*result)
