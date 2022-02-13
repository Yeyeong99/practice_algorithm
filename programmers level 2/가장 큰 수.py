from itertools import permutations
def solution(numbers):
    numbers = list(map(str, list(numbers)))
    if 0 not in numbers:
        answer = max(list(map(lambda x: ''.join(x), list(permutations(numbers, len(numbers))))))
        return answer
    else:
        new_numbers = [i for i in numbers if i != '0']
        answer = max(list(map(lambda x: ''.join(x), list(permutations(new_numbers, len(new_numbers))))))
        zero = '0' * new_numbers.count('0')
        return answer + zero
