def solution(s, n):
    capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = list(map(lambda x: x.lower(), capital))
    new_s = list(s)
    answer = ''
    for character in new_s:
        if character.islower():
            answer += lower[(lower.index(character)+n) % len(lower)]
        elif character.isupper():
            answer += capital[(capital.index(character)+n) % len(lower)]
        else:
            answer += character
    return answer
  
  # ord()를 이용해 알파벳 리스트를 생성하지 않고도 풀 수 있다.
