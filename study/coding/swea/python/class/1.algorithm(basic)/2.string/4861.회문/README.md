# ⭐max(str2.count(i) for i in str1)⭐

```python
for k in range(M//2) : # 회문 길이만큼 확인하기
    if matrix[i][j + k] != matrix[i][j + (M-1-k)] : # k 랑 M-1-k 대응
        break
```
