import sys

n = int(sys.stdin.readline().rstrip())
card_list = [i for i in range(1,n+1)]

while len(card_list) > 1:
    if len(card_list) % 2: 
        t = [card_list[-1]]
        t.extend(card_list[1::2])
        card_list = t

    else:
        card_list = card_list[1::2]


print(card_list[0])