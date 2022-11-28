#include "fem.hpp"
#include "functions.h"

const std::vector<double> get_x(
    const double start,
    const double end,
    const int n
) {
    const double h = (end - start) / n;

    std::vector<double> x;
    for (double xx = start; xx <= end; xx += h) {
        x.push_back(xx);
    }

    return x;
}

int main(const int argc, const char *argv[]) {
    if (argc != 2) {
        return EXIT_FAILURE;
    }
    const int n = atoi(argv[1]);

    const double start = 0;
    const double end = 1;
    const FEM fem = FEM(
        start, end,
        n,
        p, q, f
    );
    const std::vector<double> x = get_x(start, end, n);
    const std::vector<double> u = fem.get_u(x);
    

    for (int i = 0; i < x.size(); i++) {
        std::cout << x[i] << " " << u[i] << std::endl;
    }
}