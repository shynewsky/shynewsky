#include <iostream>
using namespace std;

int main(){
    int y, m, d;
    cin >> y >> m >> d;
    int h = (y + m + d) / 100;
    if (h % 2 == 0) cout << "대박";
    else cout << "그럭저럭";
    return 0;
}