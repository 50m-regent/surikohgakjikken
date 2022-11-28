#include <cmath>

const double p(const double x) {
    return exp(-x * x);
}

const double q(const double x) {
    return -6 * exp(-x * x);
}

const double f(const double x) {
    return -16 * x * exp(-x * x);
}