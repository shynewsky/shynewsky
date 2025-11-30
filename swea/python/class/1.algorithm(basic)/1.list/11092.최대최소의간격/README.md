### max() 구현

```python
    max_num = arr[0]
    min_num = arr[0]
    max_idx = 0
    min_idx = 0
    
    for i in range(N) :
        if max_num <= arr[i] :
            max_num = arr[i]
            max_idx = i
        if min_num > arr[i] :
            min_num = arr[i]
            min_idx = i
```