#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int cnt[24] = {0};
    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        cnt[x]++;
    }

    for (int i = 1; i <= 23; ++i){
        cout << cnt[i] << ' ';
    }

    return 0;
}