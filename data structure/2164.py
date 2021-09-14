import sys

n = int(sys.stdin.readline().rstrip())
card_list = [i for i in range(1,n+1)]

i = 1
while len(card_list) > 1:
    if i % 2: 
        del card_list[0]
    else:
        card = card_list[0]
        del card_list[0]
        card_list.append(card)
    i += 1

print(card_list[0])