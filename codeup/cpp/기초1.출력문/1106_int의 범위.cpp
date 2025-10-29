#include <iostream>
using namespace std;

int main() {
    long long val = 1 << 31;
    int min_val = val * (-1);
    int max_val = val - 1;

    cout << min_val << endl << max_val; // -2147483648  // 2147483647

    return 0;
}
