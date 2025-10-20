## 1️⃣ 내 코드

```python
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
```
<hr>

## 2️⃣ 시간복잡도 분석

- 이미 효율적으로 설계되어 있다
- 별도 최적화가 필요 없을 정도로 시간 복잡도가 낮다


- answer_dict 초기화 : O(N)
- reported_dict 초기화 : O(N)
- 첫번째 for 루프 : O(M)
- 두번째 for 루프 : O(N+R)
- 세번째 for 루프 : O(N)


- 총 시간복잡도 = O(N+M)

<hr>

## 3️⃣ 효율적인 코드

```python
def solution(id_list, report, k):
    # answer_list = []
    answer_dict = {i:0 for i in id_list}
    reported_dict = {i:set() for i in id_list}
    
    for message in report:
        send, receive = message.split()
        reported_dict[receive].add(send)
        
    for key, value in reported_dict.items():
        if len(value) >= k:
            for reporter in value:
                answer_dict[reporter] += 1
                
    # for key, value in answer_dict.items():
    #     answer_list.append(value)
    answer_list = [answer_dict[user_id] for user_id in id_list]

    return answer_list
```