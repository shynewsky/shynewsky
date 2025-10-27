#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        if (i % 3 == 0) cout << 'X' << ' ';
        else cout << i+1 << ' ';
    }


    return 0;
}