# 이중반복문

```cpp

    for(int i=0; i<5; i++){
        for(int j=0; j<5; j++){
            if(cpr[i] == basic_order[j]){
                answer[i] = j+1;
                break;
            }
        }
    }
    
    // answer 백터는 i로 순회하면서, basic_order 벡터는 j로 순회한다
    // 값이 같은 경우, answer 벡터의 값을 숫자로 대입하는데 (0~4)가 아닌 (1~5)로 대입해라

```