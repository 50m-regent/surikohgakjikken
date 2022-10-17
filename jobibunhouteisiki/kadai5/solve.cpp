#include <iostream>
#include <iomanip>
#include <cmath>

constexpr double alpha = 2;
constexpr double beta = 1;
constexpr double u0 = 1;

double uexact(double t) {
    double C = u0 - beta / alpha;
    return C * exp(-alpha * t) + beta / alpha;
}

void solve(double (*f)(double , double), double u, double dt, double start, double end) {
    std::cout<<std::fixed<<std::setprecision(16);
    double t;
    double lastu = uexact(t - dt);
    for (t = start; t < end; t += dt) {
        std::cout<<t<<" "<<u<<std::endl;
        double utemp = u;
        u = lastu + 2 * dt * f(t, u);
        lastu = utemp;
    }
    std::cout<<t<<" "<<u<<std::endl;
}

double f(double t, double u) {
    return -alpha * u + beta;
}

int main(int argc, char *argv[]) {
    if (argc != 3) return 1;

    double dt = atof(argv[1]);
    double start = 0;
    double end = atof(argv[2]);
    solve(f, 1, dt, start, end);
}