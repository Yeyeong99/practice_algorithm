import sys

stack_list = []
def push(num):
    stack_list.append(num);
    
def pop():
    if len(stack_list) != 0:
        data = stack_list[-1]
        del stack_list[-1]
    else:
        data = -1
    return data

def size():
    return len(stack_list)

def empty():
    return 1 if len(stack_list) == 0 else 0

def top():
    return stack_list[-1] if len(stack_list) != 0 else -1

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    input_split = sys.stdin.readline().rstrip().split()
    order = input_split[0]
    
    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())


# for i in range(n):
#     try:
#         order, number = input().split()
#         print(order)
#     except:
#         order = input()
#         print(order)
#     number = int(number)
#     if order == "push":
#         push(number)
#         print(stack_list, order)
#     elif order == "pop":
#         print(pop())
#         print(stack_list, order)
#     elif order == "size":
#         print(size())
#         print(stack_list, order)
#     elif order == "empty":
#         print(empty())
#         print(stack_list, order)
#     elif order == "top":
#         print(top())
#         print(stack_list, order)
    