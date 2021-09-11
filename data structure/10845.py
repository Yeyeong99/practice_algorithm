import sys
queue_list = []

def push(n):
    queue_list.append(n)

def pop():
    if len(queue_list) != 0:
        answer = queue_list[0] 
        del queue_list[0]
        return answer
    else: 
        return -1 

def size():
    return len(queue_list)

def empty():
    return 1 if len(queue_list) == 0 else 0

def front():
    return -1 if len(queue_list) == 0 else queue_list[0]

def back():
    return -1 if len(queue_list) == 0 else queue_list[-1]


n = int(sys.stdin.readline().rstrip())


for i in range(n):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == "push":
        push(int(order[1]))
    elif order[0] == "pop":
        print(pop())
    elif order[0] == "size":
        print(size())
    elif order[0] == "empty":
        print(empty())
    elif order[0] == "front":
        print(front())
    elif order[0] == "back":
        print(back())