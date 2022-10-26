#include <iostream>
#include <iomanip>
#include <cmath>

constexpr double alpha = 10;
constexpr double beta = 1;

void crank(double (*f)(double , double), double u, double dt, double start, double end) {
    std::cout<<std::fixed<<std::setprecision(16);
    double t;
    for (t = start; t < end; t += dt) {
        std::cout<<t<<" "<<u<<std::endl;
        
        u = ((2.0 - alpha * dt) * u + 2.0 * beta * dt) / (2.0 + alpha * dt);
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
    crank(f, 1, dt, start, end);
}