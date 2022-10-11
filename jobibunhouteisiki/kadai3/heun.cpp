#include <iostream>
#include <iomanip>
#include <cmath>

double uexact(double t) {
    return std::exp(t);
}

double heun(double (*f)(double , double), double u, double dt, double start, double end) {
    for (double t = start; t <= end + 1e-7; t += dt) {
        double u_ = u + f(t, u) * dt;
        u += (f(t, u) + f(t + dt, u_)) * dt / 2.0;
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
    for (int n = 1; n < 20; n++) {
        double dt = 1.0 / n;
        double u = heun(f, 1, dt, start, end);
        std::cout<<std::fixed<<std::setprecision(16)<<dt<<" "<<E(u, uexact(end))<<std::endl;
    }
}