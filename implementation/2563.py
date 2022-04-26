num = int(input())
spots = []
for i in range(num):
  x, y = map(int, input().split())
  spots.append((x, y))

over = 0

# for i in range(1, num):
#   x, y = spots[i-1]
#   for j in spots[i:]:
#     if x 
