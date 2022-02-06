# 틀린 풀이
def solution(n, lost, reserve):
    lost = set(lost) - set(reserve)
    reserve = set(reserve)-set(lost)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    return n-len(lost)

# 통과
def solution(n, lost, reserve):
  reserve_n = list(set(reserve) - set(lost))
  lost_n = list(set(lost) - set(reserve)) 
  students = n - len(lost_n)

  for i in reserve_n:
      if i - 1 in lost_n:
          students += 1
          lost_n.remove(i - 1)
      elif i + 1 in lost_n:
          students += 1
          lost_n.remove(i + 1)

  return students
