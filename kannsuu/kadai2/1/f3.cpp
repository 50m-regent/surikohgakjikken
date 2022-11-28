#include "f3.hpp"
#include "lagrange.hpp"

int main(const int argc, const char *argv[]) {
    if (argc != 4) {
        return EXIT_FAILURE;
    }
    const double start = atof(argv[1]);
    const double end = atof(argv[2]);
    const int n = atoi(argv[3]);

    Lagrange(f3, start, end, n).print_interpolated(0.001);
}