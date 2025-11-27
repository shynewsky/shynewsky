#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;

    //int num_diagonal = n * n - 3 / 2;
    int num_diagonal = n * (n - 3) / 2;

    cout << num_diagonal << endl;
    return 0;
}
