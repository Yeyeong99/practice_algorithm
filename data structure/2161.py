import sys

n = int(sys.stdin.readline().rstrip())
num_list = [i for i in range(1, n+1)]

def abandon_card(_list):
    ad_card = []
    while len(_list):
        if len(_list) == 1:
            break
        else:
            a = _list[0]
            ad_card.append(a)
            b = _list[1]
            del _list[0]
            del _list[0]
            _list.append(b)
    for i in ad_card:
        print(i)
    print(_list[0])


abandon_card(num_list)
