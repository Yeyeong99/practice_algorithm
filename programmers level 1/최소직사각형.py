def solution(sizes):
    sizes_ch = list(map(lambda x: [max(x), min(x)], sizes))
    height = []
    width =  []
    for i, j in sizes_ch:
        height.append(i)
        width.append(j)
    
    return max(height) * max(width)

# sizes의 각각의 원소에서 min값, max 값만 따로 골라 리스트로 만드는 과정을 한 줄로 나타낼 수 있음.
