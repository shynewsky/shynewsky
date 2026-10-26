# ⭐문자열 인덱스로 16진수를 접근할 수 있다⭐

### 문자열을 사용해서 "인덱스 = 번호" 를 지정할 수 있다

```python
def hex_to_bin(characters):
    hex_str = '0123456789ABCDEF'
    answer = ''
    for char in characters:
        hex_dec = hex_str.index(char)  # 해당 글자의 인덱스를 찾아서 십진수로 변환
        hex_bin = dec_to_bin(hex_dec)  # 십진수를 이진수로 변환
        answer += hex_bin

    return answer
```