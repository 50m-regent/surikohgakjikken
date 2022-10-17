#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <string>

constexpr double sigma = 10;
constexpr double b = 8.0 / 3.0;
constexpr double r = 28;

void runge_kutta(
    double (*fx)(double , double, double),
    double (*fy)(double , double, double),
    double (*fz)(double , double, double),
    double x,
    double y,
    double z,
    double dt,
    double start,
    double end
) {
    std::cout<<std::setprecision(16);

    double t;
    for (t = start; t < end; t += dt) {
        std::cout<<t<<" "<<x<<" "<<y<<" "<<z<<std::endl;

        double fx1 = fx(x, y, z);
        double fy1 = fy(x, y, z);
        double fz1 = fz(x, y, z);

        double fx2 = fx(x + fx1 * dt / 2.0, y + fy1 * dt / 2.0, z + fz1 * dt / 2.0);
        double fy2 = fy(x + fx1 * dt / 2.0, y + fy1 * dt / 2.0, z + fz1 * dt / 2.0);
        double fz2 = fz(x + fx1 * dt / 2.0, y + fy1 * dt / 2.0, z + fz1 * dt / 2.0);

        double fx3 = fx(x + fx2 * dt / 2.0, y + fy2 * dt / 2.0, z + fz2 * dt / 2.0);
        double fy3 = fy(x + fx2 * dt / 2.0, y + fy2 * dt / 2.0, z + fz2 * dt / 2.0);
        double fz3 = fz(x + fx2 * dt / 2.0, y + fy2 * dt / 2.0, z + fz2 * dt / 2.0);

        double fx4 = fx(x + fx3 * dt, y + fy3 * dt, z + fz3 * dt);
        double fy4 = fy(x + fx3 * dt, y + fy3 * dt, z + fz3 * dt);
        double fz4 = fz(x + fx3 * dt, y + fy3 * dt, z + fz3 * dt);

        x += (fx1 + 2 * fx2 + 2 * fx3 + fx4) * dt / 6.0;
        y += (fy1 + 2 * fy2 + 2 * fy3 + fy4) * dt / 6.0;
        z += (fz1 + 2 * fz2 + 2 * fz3 + fz4) * dt / 6.0;   
    }

    std::cout<<t<<" "<<x<<" "<<y<<" "<<z<<std::endl;
}

double fx(double x, double y, double z) {
    return sigma * (y - x);
}

double fy(double x, double y, double z) {
    return r * x - y - x * z;
}

double fz(double x, double y, double z) {
    return x * y - b * z;
}

int main() {
    const double start = 0, end = 100, dt = 0.01, epsilon = 0;
    double x = 1 + epsilon, y = 0, z = 0;
    runge_kutta(fx, fy, fz, x, y, z, dt, start, end);
}