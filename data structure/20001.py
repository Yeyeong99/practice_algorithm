n = input()

quest_list = []
while True:
    quest = input()
    if quest == "문제":
        quest_list.append(quest)
    elif quest == "고무오리":
        if len(quest_list) != 0:
            quest_list.pop()
        else:
            quest_list.append(quest)
            quest_list.append(quest)
    elif quest == "고무오리 디버깅 끝":
        break

if len(quest_list) == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")