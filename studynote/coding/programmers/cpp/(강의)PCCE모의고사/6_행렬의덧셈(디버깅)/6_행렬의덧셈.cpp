#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> matrix_A, vector<vector<int>> matrix_B) {
    vector<vector<int>> answer(matrix_A.size(), vector<int>(matrix_A[0].size()));
    // 벡터를 원소로 하는 벡터는 이차원벡터로, 행렬을 뜻하며 [i][j]로 원소표현 가능

    for(int i = 0; i < answer.size(); i++){
        for(int j = 0; j < answer[0].size(); j++){
            answer[i][j] = matrix_A[i][j] + matrix_B[i][j]; // 수정된 부분
        }
    }
    return answer;
}
