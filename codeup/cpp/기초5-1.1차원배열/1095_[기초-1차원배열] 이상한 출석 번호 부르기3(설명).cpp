#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int x, minVal = 100;
    for (int i = 0; i < n; i++){
        cin >> x;
        if (minVal > x) {
            minVal = x;
        }
    }
    cout << minVal;

    return 0;
}