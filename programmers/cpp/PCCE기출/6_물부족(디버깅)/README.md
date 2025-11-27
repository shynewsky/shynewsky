# 문제해석

```cpp

// storage : 현 저수지 물양 = 총 사용가능한 물 양
// usage : 지난달 물 사용량 = 필요한 물 양
// change<> : 물 사용 변화량 정수 리스트
// 저수지의 사용한 물의 양이 많아야, 몇개월 빼 사용하면서도 부족해지지 않는다

    for(int i=0; i<change.size(); i++){ // 원소 개수만큼 순회
        usage = usage + (usage * change[i] / 100); // 지난달 물의 양에서 퍼센트만큼 증감
        total_usage += usage;	// 총 물 사용량 누적
        if(total_usage > storage){ // 부족해진다면 >> 현재 달 반환
            return i;
        }
    }
    return -1; // 1년간 부족해지지 않는다면 >> -1 반환

```