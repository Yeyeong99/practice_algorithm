n = int(input())
pairs = int(input())

graphs = [[] for i in range(n+1)]

for pair in range(pairs):
  node1, node2 = map(int, input().split())
  graphs[node1].append(node2)
  graphs[node2].append(node1)

graphs = list(map(lambda x: sorted(x), graphs))

from collections import deque

def bfs(sequence, visited):
  queue = deque([1])
  visited[1] = True

  count = 0
  while queue:
    v = queue.popleft()
    count += 1

    for i in sequence[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
  return count - 1 # 1 번 제외

visited = [False] * (n+1)
print(bfs(graphs, visited))
