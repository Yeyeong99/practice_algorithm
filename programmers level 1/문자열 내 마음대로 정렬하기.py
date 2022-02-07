def solution(strings, n):
    string_list = [[string, string[n]] for string in strings]
    string_list.sort(key=lambda x: (x[1], x[0]))
    return [string[0] for string in string_list]
  
  # sort에서 정렬을 기준을 두 개로 하기 위해선 tuple을 이용함
