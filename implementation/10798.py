words = []

for i in range(5):
  word = input()
  words.append(word)

max_len = max(list(map(lambda x: len(x), words)))
new_words = []
for i in range(max_len):
  for j in words:
    try:
      new_words.append(j[i])
    except:
      continue

print(''.join(new_words))
