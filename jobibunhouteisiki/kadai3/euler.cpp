#include <iostream>
#include <iomanip>
#include <cmath>

double euler(double (*f)(double , double), double u, double dt, double start, double end) {
    for (double t = start; t <= end; t += dt) {
        u += f(t, u) * dt;
    }

    return u;
}

double E(double u, double uexact) {
    return std::fabs(u - uexact);
}

double f(double t, double u) {
    return u;
}

double uexact(double t) {
    return std::exp(t);
}

int main() {
    double start = 0, end = 1;
    for (int n = 1; n < 100; n *= 2) {
        double dt = 1.0 / n;
        double u = euler(f, 1, dt, start, end);
        std::cout<<std::fixed<<std::setprecision(10)<<dt<<" "<<E(u, uexact(end))<<std::endl;
    }
}