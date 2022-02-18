def solution(n):
    count = 0
    for i in range(1, n+1):
        n_sum = 0
        while True:
            n_sum += i
            if n_sum == n:
                count += 1
                break
            elif n_sum > n:
                break
            i += 1
    
    return count
  
  # elif 안쓰면 시간초과
