# -*- coding: utf-8 -*-
"""프로그래머스_완주하지 못한 선수.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18tk36TqNt-4iiP_xksxbv6Y3NRcWGCxK
"""

# 틀린 답 - 마지막 return 이 for 문 안에 있기 때문에, 3번 째 예시로 가기 전에 2번째에서 끝나버림
# 마지막 return이 for 문 밖에 있는 경우, participant를 기준으로 잡았기 때문에 completion에서 오류가 날 것.
def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(participant, completion)
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]
        return participant[-1]

# 정답
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]