import sys

dec = []
def push_front(n):
    dec.insert(0,n)

def push_back(n):
    dec.append(n)

def pop_front():
    if len(dec) == 0:
        result = -1
    else:
        result = dec[0]
        del dec[0]
    return result

def pop_back():
    return -1 if len(dec) == 0 else dec.pop()

def size():
    return len(dec)

def empty():
    return 1 if len(dec) == 0 else 0

def front():
    return -1 if len(dec) == 0 else dec[0]

def back():
    return -1 if len(dec) == 0 else dec[-1]

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    order = sys.stdin.readline().rstrip().split()
    j = order[0]
    if j == "push_back":
        push_back(order[1])
    elif j == "push_front":
        push_front(order[1])
    elif j == "pop_front":
        print(pop_front())
    elif j == "pop_back":
        print(pop_back())
    elif j == "size":
        print(size())
    elif j == "empty":
        print(empty())
    elif j == "front":
        print(front())
    elif j == "back":
        print(back())
