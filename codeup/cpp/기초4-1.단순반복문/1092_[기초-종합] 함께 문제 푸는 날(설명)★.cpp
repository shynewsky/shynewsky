#include <iostream>
using namespace std;

long long gcd(long long x, long long y) {
    while (y) {
        long long r = x % y;
        x = y;
        y = r;
    }
    return x;
}

long long lcm(long long x, long long y) {
    return x / gcd(x, y) * y;  // 오버플로 줄이기 위해 x를 먼저 나눔
}

int main() {
    long long a, b, c;
    cin >> a >> b >> c;

    long long abc = lcm(lcm(a, b), c);
    cout << abc;
    return 0;
}
