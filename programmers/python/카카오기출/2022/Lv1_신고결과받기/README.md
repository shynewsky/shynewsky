## 시간복잡도 분석

- 이미 효율적으로 설계되어 있다
- 별도 최적화가 필요 없을 정도로 시간 복잡도가 낮다


- answer_dict 초기화 : O(N)
- reported_dict 초기화 : O(N)
- 첫번째 for 루프 : O(M)
- 두번째 for 루프 : O(N+R)
- 세번째 for 루프 : O(N)


- 총 시간복잡도 = O(N+M)
