n = int(input())

minion_dict = {}

for i in range(n):
    eng_minion = input().split(" = ")
    minion_dict[eng_minion[0]] = eng_minion[1]

t = int(input())

for j in range(t):
    k = int(input())
    sentence = input().split()
    for x in sentence:
        completed_sen = []
        word = minion_dict[f"{x}"]
        completed_sen.append(word)
        print(" ".join(completed_sen))
