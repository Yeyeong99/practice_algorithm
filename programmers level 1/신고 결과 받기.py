def solution(id_list, report, k):
    id_dict = {i: 0 for i in id_list}
    report_dict = {}
    for i in report:
        user, rp_user = i.split()
        if rp_user not in report_dict:
            report_dict[rp_user] = [user]
        elif user not in report_dict[rp_user]:
            report_dict[rp_user].append(user)
    
    for i in report_dict.values():
        if len(i) >= k:
            for j in i:
                id_dict[j] += 1
        
    return list(id_dict.values())
  
  # index를 활용하면 dictionary를 두 개 만들지 않고 해결할 수 있음
