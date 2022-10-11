#include <iostream>
#include <iomanip>
#include <cmath>

double uexact(double t) {
    return std::exp(t);
}

double adams_second(double (*f)(double , double), double u, double dt, double start, double end) {
    double lastf = uexact(start - dt);
    for (double t = start; t <= end; t += dt) {
        u += (3.0 * f(t, u) - lastf) * dt / 2.0;
        lastf = f(t, u);
    }

    return u;
}

double E(double u, double uexact) {
    return std::fabs(u - uexact);
}

double f(double t, double u) {
    return u;
}

int main() {
    double start = 0, end = 1;
    for (double dt = 1e-7; dt <= 1; dt *= 10) {
        double u = adams_second(f, 1, dt, start, end);
        std::cout<<std::fixed<<std::setprecision(10)<<dt<<" "<<E(u, uexact(end))<<std::endl;
    }
}