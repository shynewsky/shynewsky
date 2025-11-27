#include <string>
#include <vector>

using namespace std;

vector<int> solution(string menu, int n) {
    vector<int> tomato_pasta = {4, 4, 1, 125};
    vector<int> shrimp_oil_pasta = {6, 3, 0, 170};
    vector<int> mushroom_cream_pasta = {5, 4, 1, 140};
    vector<int> answer = {0, 0, 0, 0};

    if(menu == "tomato pasta"){
        for(int i = 0; i < 4; i++){
            answer[i] = tomato_pasta[i] * n; // 벡터 원소 그대로 곱해서 대입가능
        }
    }
    else if(menu == "shrimp oil pasta"){
        for(int i = 0; i < 4; i++){
            answer[i] = shrimp_oil_pasta[i] * n; // 벡터 원소 그대로 곱해서 대입가능
        }
    }
    else if(menu == "mushroom cream pasta"){
        for(int i = 0; i < 4; i++){
            answer[i] = mushroom_cream_pasta[i] * n; // 벡터 원소 그대로 곱해서 대입가능
        }
    }
    return answer;
}

