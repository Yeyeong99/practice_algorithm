from collections import Counter
n = int(input())

nums = []
for i in range(n):
  num = int(input())
  nums.append(num)

print(round(sum(nums)/n))
print(sorted(nums)[n//2])
c_nums = dict(Counter(nums))

for i in c_nums:
  if cmax(c_nums.values())

print(sorted(nums)[-1]-sorted(nums)[0])
