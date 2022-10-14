#include <iostream>
#include <iomanip>
#include <cmath>

#define ALPHA 2.0
#define BETA 1.0
#define U0 1.0

double uexact(double t) {
    double C = U0 - BETA / ALPHA;
    return C * exp(-ALPHA * t) + BETA / ALPHA;
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
    return -ALPHA * u + BETA;
}

int main(int argc, char *argv[]) {
    if (argc != 3) return 1;

    double dt = atof(argv[1]);
    double start = 0;
    double end = atof(argv[2]);
    solve(f, 1, dt, start, end);
}