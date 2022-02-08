def solution(s):
    s_list = s.split(" ")
    answer = []
    for word in s_list:
        new_word = ''
        for idx, w in enumerate(word):
            if idx % 2 == 0:
                new_word += w.upper()
            else:
                new_word += w.lower()
        answer.append(new_word)
    
    return ' '.join(answer)
 
# split에 " "를 넘겨주지 않아 오류가 났었다.
