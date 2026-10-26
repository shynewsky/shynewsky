#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int board[20][20] = {0};

    // 입력
    for (int k = 0; k < n; k++){
        int x, y;
        cin >> x >> y;
        if (1 <= x && x <= 19 && 1 <= y && y <= 19){
            board[x][y] = 1;
        }
    }

    // 출력
    for (int i = 1; i <= 19; i++){
        for (int j = 1; j <= 19; j++){
            if (j > 1) cout << ' ';
            cout << board[i][j];
        }
        cout << '\n';
    }

    return 0;
}