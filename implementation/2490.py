lines = []
for i in range(3):
  line = input()
  lines.append(line)

for i in lines:
  if i.count('0') == 4:
    print('D')
  elif i.count('0') == 3:
    print('C')
  elif i.count('0') == 2:
    print('B')
  elif i.count('0') == 1:
    print('A')
  else:
    print('E')
 
