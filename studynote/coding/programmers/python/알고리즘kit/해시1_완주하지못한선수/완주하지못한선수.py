def solution(participant, completion):
    total = {}

    for person in participant:
        total[person] = total.get(person, 0) + 1

    for person in completion:
        total[person] -= 1

    for person, count in total.items():
        if count > 0:
            return person