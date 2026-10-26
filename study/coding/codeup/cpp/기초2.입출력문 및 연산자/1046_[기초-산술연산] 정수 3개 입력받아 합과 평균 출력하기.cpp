#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    long long a, b, c;
    cin >> a >> b >> c;
    
    long long sum = a + b + c;
    double avg = sum / 3.0;
    cout << sum << '\n';
    cout << fixed << setprecision(1) << avg;
    
    return 0;
}