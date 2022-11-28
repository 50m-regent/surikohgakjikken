#include <iostream>
#include <cmath>
#include <iomanip>

#include "gauss.hpp"
#include "2.hpp"

int main(const int argc, const char *argv[]) {
    std::cout << std::fixed << std::setprecision(16);

    const double start = 0;
    const double end = 1;
    const int M = 2;
    const std::vector<double> y{-1.0 / sqrt(3.0), 1.0 / sqrt(3.0)};
    const std::vector<double> w{1.0, 1.0};

    for (int i = 0, n = 1; i <= 10; i++, n *= 2) {
        std::cout << n << " " << gauss(f, start, end, n, M, y, w) << std::endl;
    }
}