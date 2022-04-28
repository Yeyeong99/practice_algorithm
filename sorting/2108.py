from collections import Counter
n = int(input())

nums = []
for i in range(n):
  num = int(input())
  nums.append(num)

print(round(sum(nums)/n))
print(sorted(nums)[n//2])
c_nums = dict(Counter(nums))

freqs = []
for i in c_nums.keys():
  if c_nums[i] == max(c_nums.values()):
    freqs.append(i)

freqs.sort()
if len(freqs) == 1:
  print(freqs[0])
else:
  print(freqs[1])
  

print(sorted(nums)[-1]-sorted(nums)[0])
