# ⭐ .equals()

- “두 값이 같은지”를 비교하는 함수
- 특히 문자열(String)을 비교할 때 반드시 써야 하는 메서드

### 📍 == (주소 비교)

```java
String a = ">";
String b = new String(">");

System.out.println(a == b); // false
```

### 📍 equals() (내용 비교)

```java
System.out.println(a.equals(b)); // true
```
