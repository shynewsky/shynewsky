# 알고리즘 확인하기

```cpp
    for (int i = 0; i < num_student; i++) {
        if (our_score[i] == score_list[numbers[i]-1]) {
        // 학생수를 번호로 순서로 가져가는 것이 아니라, 학생번호를 순서로 가져가야한다
            answer[i] = "Same";
        }
        else {
            answer[i] = "Different";
        }
    }
```