# ⭐ re 모듈 사용방법 ⭐

- 파이썬의 정규 표현식 기능을 제공하는 표준 라이브러리
- <ins>**문자열에서 패턴을 찾거나, 교체하거나, 분리할때 사용**</ins>

```python
# 기본구조
import re

pattern = r"정규식패턴"
result = re.메서드(pattern, 대상문자열)
```

- 주요함수

| | |
|---|---|
|re.match(pattern, string) |문자열의 처음부터 패턴이 일치하는지 확인 |
|re.search(pattern, string) |문자열 전체에서 처음으로 일치하는 부분을 찾음 |
|re.findall(pattern, string) |일치하는 모든 문자열을 리스트로 반환 |
|re.finditer(pattern, string) |일치하는 모든 부분을 Match 객체의 반복자(iterator) 형태로 반환 |
|re.sub(pattern, repl, string) |일치하는 부분을 다른 문자열로 치환 |
|re.split(pattern, string) |패턴을 기준으로 문자열 분리 |

```python
# 기본 예시
import re

text = "My phone number is 010-1234-5678."

# 숫자만 추출
numbers = re.findall(r"\d+", text)
print(numbers)   # ['010', '1234', '5678']

# 전화번호 형태 찾기
match = re.search(r"\d{3}-\d{4}-\d{4}", text)
print(match.group())  # 010-1234-5678

# 문자열 치환
new_text = re.sub(r"\d", "*", text)
print(new_text)  # My phone number is ***-****-****.​
```

- 자주 사용하는 정규식 패턴

|패턴|의미|예시|
|---|---|---|
|. |모든 문자 1개 |a.c → “abc”, “a#c” 등 |
|\d	|숫자(0–9) |\d\d\d → “123” |
|\w	|영문자·숫자·밑줄(_) |\w+ → “word123” |
|\s |공백 문자 |\s+ → “ ” |
|^ |문자열 시작 |^Hello |
|$ |문자열 끝 |world$ |
|[]	|반복 횟수 |\d{2,4} → 2~4자리 숫자 |
|` |` |OR 조건 |
|() |그룹 지정 |(abc)+ |

- 활용 예시

```python
# 이메일 추출
text = "Contact us at help@company.com or info@brand.co.kr"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails) # ['help@company.com', 'info@brand.co.kr']
```

```python
# HTML 태그 제거
html = "<h1>Hello</h1><p>World</p>"
clean = re.sub(r"<.*?>", "", html)
print(clean) # HelloWorld
```

```python
# 문자열 검사
password = "abc123"
if re.match(r"^[A-Za-z0-9]{6,12}$", password):
    print("유효한 비밀번호 형식입니다.")
else:
    print("형식이 올바르지 않습니다.")
```

```python
# 컴파일 방식(고급)
pattern = re.compile(r"\d{3}-\d{4}-\d{4}")
for text in ["010-1234-5678", "02-123-4567"]:
    if pattern.match(text):
        print("휴대폰 번호:", text)
```


