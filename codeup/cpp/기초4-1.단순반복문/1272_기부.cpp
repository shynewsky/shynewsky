#include <iostream>
using namespace std;

int main(){
    int n, t;
    cin >> n;
    int m = 0;
    for (int i = 0; i < n; i++){
        cin >> t;
        if (m < t) m = t;
    }
    cout << m;
    return 0;
}