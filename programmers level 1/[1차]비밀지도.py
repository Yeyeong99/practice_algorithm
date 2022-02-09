def solution(n, arr1, arr2):
    def change_digit(num):
        new_num = ''
        while num > 0:
            new_num += str(num % 2)
            num //= 2
        return '0' * (n-len(new_num)) + new_num[::-1]
    n_arr1 = list(map(lambda x: change_digit(x), arr1))
    n_arr2 = list(map(lambda x: change_digit(x), arr2))
    answer = []
    print(n_arr1, n_arr2)
    for i, j in zip(n_arr1, n_arr2):
        word = ''    
        for x, y in zip(i, j):
            if x == '1' or y == '1':
                word += '#'
            else:
                word += ' '
        answer.append(word)
    return answer
  
  # 문자열 뒤집기 [::-1]
  # bin 함수
