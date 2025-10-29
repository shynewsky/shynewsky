#include <iostream>
using namespace std;

int main(){
    long long a, r, n; // 오버플로우 발생
    cin >> a >> r >> n;
    for (int i=1; i<n; i++) a *= r; // C++ 에는 제곱이 없다
    cout << a;
    return 0;
}