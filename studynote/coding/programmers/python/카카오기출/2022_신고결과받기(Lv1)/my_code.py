def solution(id_list, report, k):
    answer_list = []
    answer_dict = {i: 0 for i in id_list}
    reported_dict = {i: set() for i in id_list}

    for message in report:
        send, receive = message.split()
        reported_dict[receive].add(send)

    for key, value in reported_dict.items():
        if len(value) >= k:
            for reporter in value:
                answer_dict[reporter] += 1

    for key, value in answer_dict.items():
        answer_list.append(value)

    return answer_list
