def solution(N, stages):
    stage_dict = {stage: 0 for stage in range(1, N+1)}
    for key in stage_dict:
        try:
            fail_players = stages.count(key)
            players = [stage for stage in stages if stage >= key]
            stage_dict[key] = fail_players / (len(players))
        except:
            stage_dict[key] = 0
    
    answer = list(stage_dict.items())
    answer.sort(key=lambda x: x[1], reverse=True)
    return [i[0] for i in answer]
  
# count의 시간복잡도가 O(n) -> 시간복잡도 줄이는 방법으로 생각해보기
# len(stages) - fail_players 이런 식으로 빼주면 list comprehension을 이용하지 않아도 됨
