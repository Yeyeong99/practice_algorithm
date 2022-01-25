n, m, v = map(int, input().split())
road = [[] for i in range(n)]

for i in range(m):
  v1, v2 = map(int, input().split())
  road[v1-1].append(v2)

dfs = [] 
for i in road:
  if len(road[v-1]) > 0:
    dfs.append(road[v-1][0])
    print(v)
    v = road[v-1][0]
    print(v, road[v-1][0])
    road[v-1].pop(0)
  else:
    continue

dfs

