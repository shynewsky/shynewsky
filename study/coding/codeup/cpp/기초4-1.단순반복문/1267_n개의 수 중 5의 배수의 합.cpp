#include <iostream>
using namespace std;

int main(){
    int n, t;
    cin >> n;
    int s = 0;
    for (int i = 0; i < n; i ++){
        cin >> t;
        if (t % 5 == 0) s += t;
    }
    cout << s;
    return 0;
}