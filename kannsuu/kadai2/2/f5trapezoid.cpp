#include <iostream>

#include "trapezoid.hpp"
#include "f5.hpp"

int main(const int argc, const char *argv[]) {
    if (argc != 3) {
        return EXIT_FAILURE;
    }
    const double start = atof(argv[1]);
    const double end = atof(argv[2]);

    for (int i = 0, n = 1; i <= 10; i++, n *= 2) {
        std::cout << n << " " << trapezoid(f5, start, end, n) << std::endl;
    }
}