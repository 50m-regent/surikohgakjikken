#include <iostream>
#include <cmath>

#include "gauss.hpp"
#include "f4.hpp"

int main(const int argc, const char *argv[]) {
    const double start = 1;
    const double end = 2;
    const int M = 2;
    const std::vector<double> y{-1.0 / sqrt(3.0), 1.0 / sqrt(3.0)};
    const std::vector<double> w{1.0, 1.0};

    for (int i = 0, n = 1; i <= 10; i++, n *= 2) {
        std::cout << n << " " << gauss(f4, start, end, n, M, y, w) << std::endl;
    }
}