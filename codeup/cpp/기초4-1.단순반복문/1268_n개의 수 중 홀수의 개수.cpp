#include <iostream>
using namespace std;

int main(){
    int n, t;
    cin >> n;
    int c = 0;
    for (int i = 0; i < n; i ++){
        cin >> t;
        if (t % 2 == 1) c++;
    }
    cout << c;
    return 0;
}