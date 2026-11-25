#include <iostream>
using namespace std;

int main(){
    int s, e;
    cin >> s >> e;
    for (int i = s; i <= e; i++){
        if (i % 2 == 1) cout << i << ' ';
    }
    return 0;
}