#include <iostream>
#include <cstdlib>
#include <cmath>

double f(double a, double x) {
    return a * x * x + x + 1;
}

void showf(double a) {
    for (double x = 0; x < 3.0; x += 0.01) {
        std::cout << f(a, x) << std::endl;
    }
}

int main(int argc, char **argv) {
    showf(2);
    showf(3);

    return EXIT_SUCCESS;
}