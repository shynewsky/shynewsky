```python
#내가 짠 코드

def solution(participant, completion):

    for person in participant :
        if person in completion:
            completion.remove(person)
        else :
            return person

```

정확성 부문에서 모든 테스트 케이스를 통과했지만<br>
효율성 부문에서 모든 테스트 케이스를 실패했다

ChatGPT 한테 물어보니 시간복잡도 면에서 비효율적이라는 말이 나왔다<br>
in 과 remove() 모두 평균적으로 O(n) 의 시간 복잡도를 가지기 때문에<br>
중첩으로 사용하면 O(n) * O(n) = O(n^2) 이 된다는 것이다

<ins>**해시맵(딕셔너리)**</ins> 또는 
<ins>**collection 모듈의 counter**</ins> 를 사용하는 방법이 있다

<hr>

## 1️⃣ 해시맵(딕셔너리) 사용

```python
total = {}
```
- 전체 참가자를 딕셔너리로 묶어, 동명이인이 몇명씩 있는지 기록하도록 한다


```python
for person in participant :
    total[person] = total.get(person,0) + 1
```
- person : 이름이 적힌 문자열
- dict.get(key, default) : 딕셔너리에 키가 있으면 값을 반환, 키가 없으면 기본값 반환
- dict.get(key, 0) : 딕셔너리에 키가 있으면 값을 반환, 키가 없으면 0 반환
- record[person] = record.get(person,0) + 1 : 같은 이름끼리 찾아서 1씩 올린다

```python
for person in completion:
    total[person] -= 1
```
- 완주를 했으면, 해당 이름에서 한명씩 뺀다

```python
for person, count in total.items():
    if count > 0:
        return person
```
- dict.items() : 딕셔너리의 (키, 값) 쌍을 튜플 형태로 하나씩 꺼내온다
- person, count : 튜플로 꺼내온 쌍을 바로 언패킹하여, person 에는 키를, count 에는 값을 넣는다
- 완주하지 못한 사람은 count 가 남아있을 것이므로, 해당 사람을 반환한다

```python
#최종 코드

def solution(participant, completion):
    total = {}

    for person in participant:
        total[person] = total.get(person, 0) + 1

    for person in completion:
        total[person] -= 1

    for person, count in total.items():
        if count > 0:
            return person
```

<hr>

## 2️⃣ collections.Counter 사용

```python
#예시

from collections import Counter

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counted = Counter(fruits)    #Counter({'apple': 3, 'banana': 2, 'orange': 1})
```
- collection 모듈 : 기본 자료형보다 유용한 자료구조가 있다 ㅡ counter, deque, defaultDict, orderedDict, namedTuple 등
- Counter() : list 같은 자료에서 각 항목이 몇번 나왔는지 자동으로 세서 딕셔너리 형태로 반환하는 메소드

```python
p_counter = Counter(participant)
c_counter = Counter(completion)
```
- p_counter : participant 리스트에 담긴 원소를 같은 원소끼리 모아서 개수와 함께 딕셔너리로 반환한다
- c_counter : completion 리스트에 담긴 원소를 같은 원소끼리 모아서 개수와 함께 딕셔너리로 반환한다

```python
answer = p_counter - c_counter  # 남은 1명만 차이남
```
- answer : 완주 못한 사람의 수만 담긴 딕셔너리
- 원래 딕셔너리끼리는 빼기(-) 연산을 못한다. collection.Counter 로 만들어진 자료형끼리만 가능한 특별한 연산이다
- collection.Counter 끼리 빼기(-) 연산 : 같은 키가 있을경우 서로의 값을 소거하고, 값이 0이면 키까지 사라진다

```python
return list(answer.keys())[0]
```
- keys()로 answer 딕셔너리에서 남은 키를 반환한 것을 list() 에 담고, 그의 첫번째 원소[0] 를 반환한다

```python
#최종 코드

def solution(participant, completion):
    record = {}

    for person in participant:
        record[person] = record.get(person, 0) + 1

    for person in completion:
        record[person] -= 1

    for person, count in record.items():
        if count > 0:
            return person
```









