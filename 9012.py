import sys

def determine(words):
    count = 0
    isTrue = True
    for word in words:
        if word == "(":
            count += 1
        elif word == ")":
            count -= 1        
        if count < 0:
            isTrue = False
            break
    if count > 0:
        isTrue = False
    elif count == 0:
        isTrue = True
    
    return "YES" if isTrue else "NO"


n = int(sys.stdin.readline().rstrip())

for i in range(n):
    # 리스트로 저장: input_split = sys.stdin.readline().rstrip().split()
    input_split = list(sys.stdin.readline().strip())
    print(determine(input_split))