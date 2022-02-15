def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    for i, j in zip(A,B):
        answer += i*j

    return answer
  
# 효율성 테스트 통과 못함
    # while A:
    #     answer += max(A) * min(B)
    #     A.remove(max(A))
    #     B.remove(min(B))
