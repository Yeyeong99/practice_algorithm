def solution(n, m):
    n_ali = [i for i in range(1, n+1) if n % i == 0]
    m_ali = [i for i in range(1, m+1) if m % i == 0]
    ali = [i for i in n_ali if i in m_ali]
    
    return [max(ali), n * (m // max(ali))]
  
  # 유클리드 호제법
