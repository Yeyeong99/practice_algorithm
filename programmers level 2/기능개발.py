def solution(progresses, speeds):
    operations = []
    answer = [1]
    for progress, speed in zip(progresses, speeds):
        if (100-progress) % speed == 0:
            operations.append((100-progress) // speed)
        else:
            operations.append((100-progress) // speed + 1)

    for i in range(1, len(operations)):
        if operations[i-1] < operations[i]:
            answer.append(1)
        else:
            answer[-1] += 1

    return answer
