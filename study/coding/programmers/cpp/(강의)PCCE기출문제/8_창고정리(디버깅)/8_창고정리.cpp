#include <string>
#include <vector>

using namespace std;

string solution(vector<string> storage, vector<int> num) {

    // 새 정리함의 아이템 번호이다
    int num_item = 0;
    
	// 벡터 이름과 크기만 선언하고, 초기화하지 않은 상태이다
    vector<string> clean_storage(storage.size());
    vector<int> clean_num(num.size());

    for(int i=0; i<storage.size(); i++){ // i는 이전 정리함을 순회한다
        int clean_idx = -1;        
        
        for(int j=0; j<num_item; j++){ // j는 새 정리함을 순회한다
            if(storage[i] == clean_storage[j]){ 
                clean_idx = j;
                break;
            }
        }       
        if(clean_idx == -1){
            clean_storage[num_item] = storage[i]; 
            clean_num[num_item] = num[i];
            num_item += 1;
        }
        else{
            clean_num[clean_idx] += num[i];
        }
    }

    
    // 아래 코드에는 틀린 부분이 없습니다.
    
    int num_max = -1;
    string answer = "";
    for(int i=0; i<num_item; i++){
        if(clean_num[i] > num_max){
            num_max = clean_num[i];
            answer = clean_storage[i];
        }
    }
    return answer;
}
