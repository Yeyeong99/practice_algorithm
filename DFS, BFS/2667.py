# 백준 2667, 이취코 p151 참고

num = int(input())

graph = []
for i in range(num):
  line = input()
  graph.append([int(i) for i in line])

def dfs(x, y):
  if x <= -1 or x >= len(graph[0]) or y <= -1 or y >= num:
    return False

  if graph[x][y] == 0:
    graph[x][y] == 1 #  방문처리
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True

  return False

result = 0
for i in range(len(graph[0])):
  for j in range(num):
    if dfs(i, j) == True:
      result += 1

print(result)
