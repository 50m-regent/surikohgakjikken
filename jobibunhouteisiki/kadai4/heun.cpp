#include <iostream>
#include <iomanip>
#include <cmath>

#define ALPHA 10.0
#define BETA 1.0

void heun(double (*f)(double , double), double u, double dt, double start, double end) {
    std::cout<<std::fixed<<std::setprecision(16);
    double t;
    for (t = start; t < end; t += dt) {
        std::cout<<t<<" "<<u<<std::endl;
        double u_ = u + f(t, u) * dt;
        u += (f(t, u) + f(t + dt, u_)) * dt / 2.0;
        
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
    heun(f, 1, dt, start, end);
}