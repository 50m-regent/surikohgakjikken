#include <iostream>
#include <iomanip>
#include <cmath>

double uexact(double t) {
    return std::exp(t);
}

double runge_kutta(double (*f)(double , double), double u, double dt, double start, double end) {
    for (double t = start; t <= end + 1e-7; t += dt) {
        double f1 = f(t, u);
        double f2 = f(t + dt / 2.0, u + f1 * dt / 2.0);
        double f3 = f(t + dt / 2.0, u + f2 * dt / 2.0);
        double f4 = f(t + dt, u + f3 * dt);

        u += (f1 + 2 * f2 + 2 * f3 + f4) * dt / 6.0;
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
        double u = runge_kutta(f, 1, dt, start, end);
        std::cout<<std::fixed<<std::setprecision(16)<<dt<<" "<<E(u, uexact(end))<<std::endl;
    }
}