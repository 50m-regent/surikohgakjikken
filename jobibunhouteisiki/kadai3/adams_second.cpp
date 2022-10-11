#include <iostream>
#include <iomanip>
#include <cmath>

double uexact(double t) {
    return std::exp(t);
}

double adams_second(double (*f)(double , double), double u, double dt, double start, double end) {
    double lastf = uexact(start - dt);
    for (double t = start; t < end; t += dt) {
        double nowf = f(t, u);
        u += (3.0 * nowf - lastf) * dt / 2.0;
        lastf = nowf;
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
    for (int n = 1; n < 1e7; n *= 2) {
         double dt = 1.0 / n;
        double u = adams_second(f, 1, dt, start, end);
        std::cout<<std::fixed<<std::setprecision(16)<<dt<<" "<<E(u, uexact(end))<<std::endl;
    }
}