#include <string>
#include <vector>

using namespace std;

int func1(int weight){
    if(weight < 5){
        return 500;
    }
    else if(weight < 10){
        return 1000;
    }
    else{
        return 4000;
    }
}

int func2(int w, int l, int h, int we){
    if(w >= 80 || l >= 80 || h >= 80){
        return -1;
    }
    if(w+l+h >= 160){
        return -1;
    }
    if(we >= 25){
        return -1;
    }
    return 0;
}

int func3(int size){
    if(size < 80){
        return 3500;
    }
    else if(size < 100){
        return 4500;
    }
    else if(size < 120){
        return 6000;
    }
    else{
        return 12000;
    }
}

int solution(int width, int length, int height, int weight) {
    if(func2(width, length, height, weight)){ // 함수를 호출할땐, ()와 매개변수를 넣어야 한다
        return -1;
    }
    int price = func1(weight); // 함수를 호출할땐, ()와 매개변수를 넣어야 한다
    price += func3(width + length + height); // 함수를 호출할땐, ()와 매개변수를 넣어야 한다
    return price;
}

