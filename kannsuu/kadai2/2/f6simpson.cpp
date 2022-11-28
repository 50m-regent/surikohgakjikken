#include <iostream>

#include "simpson.hpp"
#include "f6.hpp"

int main(const int argc, const char *argv[]) {
    if (argc != 3) {
        return EXIT_FAILURE;
    }
    const double start = atof(argv[1]);
    const double end = atof(argv[2]);

    for (int i = 0, n = 1; i <= 10; i++, n *= 2) {
        std::cout << n << " " << simpson(f6, start, end, n) << std::endl;
    }
}