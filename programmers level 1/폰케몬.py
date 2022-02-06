def solution(nums):
    nums_set = set(nums)
    if len(nums_set) > len(nums) / 2:
        return len(nums) / 2
    else:
        return len(nums_set)
      
  # min 함수를 쓰면 한 줄로 해결할 수 있다.
