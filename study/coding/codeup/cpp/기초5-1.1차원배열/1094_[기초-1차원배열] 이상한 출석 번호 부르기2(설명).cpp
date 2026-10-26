#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int cnt[n] = {0};
    for (int i = 0; i < n; i++){
        cin >> cnt[i];
    }

    for (int i = n-1; i >= 0; i--){
        cout << cnt[i] << ' ';
    }

    return 0;
}