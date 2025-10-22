#include <iostream>
using namespace std;

int main(){
    int a;
    cin >> a;
    if (90 <= a && a <= 100) cout << "A" << "\n";
    else if (70 <= a && a <= 89) cout << "B" << "\n";
    else if (40 <= a && a <= 69) cout << "C" << "\n";
    else if (0 <= a && a <= 39) cout << "D" << "\n";
    return 0;
}