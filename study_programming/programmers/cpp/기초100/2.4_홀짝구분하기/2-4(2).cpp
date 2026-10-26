#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    
    // 코드입력
    cout << n << " is " << ( n % 2 ? "odd" : "even");

    return 0;
}
