#include <iostream>
#include <cmath>

#include "gauss.hpp"
#include "f5.hpp"

int main(const int argc, const char *argv[]) {
    const double start = -1;
    const double end = 1;
    const int M = 3;
    const std::vector<double> y{-sqrt(3.0 / 5.0), 0, sqrt(3.0 / 5.0)};
    const std::vector<double> w{5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0};

    for (int i = 0, n = 1; i <= 10; i++, n *= 2) {
        std::cout << n << " " << gauss(f5, start, end, n, M, y, w) << std::endl;
    }
}