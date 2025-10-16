#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int year,month,day;
    char dot;
    cin >> year >> dot >> month >> dot >> day;
    cout << setw(2) << setfill('0') << day << '-' 
    << setw(2) << setfill('0') << month << '-'
    << setw(4) << setfill('0') << year;
    return 0;
}
