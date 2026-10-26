#include <iostream>

using namespace std;

int main(void) {
    int age, money, complete;
    cin >> age >> money >> complete;

    if(age >= 20 && age <= 29){
        money = (money / 100) * 10;
    }
    else if(age >= 30 && age <= 39){
        money = (money / 100) * 30;
    }
    else{
        money = 0;
    }

    if(complete){
        money /= 2;
    }

    cout << money;
    return 0;
}

