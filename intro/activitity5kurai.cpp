#include <iostream>

int f(int& x) {
    return ++x;
}

int main() {
    int x = 1, n = 10;

    while (n--) {
        std::cout<<f(x)<<std::endl;
    }
    std::cout<<x<<std::endl;
    
    return EXIT_SUCCESS;
}