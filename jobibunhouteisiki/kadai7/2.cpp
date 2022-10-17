#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <string>
#include<vector>

constexpr double sigma = 10;
constexpr double b = 8.0 / 3.0;
constexpr double r = 28;

std::vector<double> x_0, y_0, z_0;

void runge_kutta_0(
    double (*fx)(double , double, double),
    double (*fy)(double , double, double),
    double (*fz)(double , double, double),
    double dt,
    double start,
    double end
) {
    double t;
    for (t = start; t < end; t += dt) {
        double fx1 = fx(x_0.back(), y_0.back(), z_0.back());
        double fy1 = fy(x_0.back(), y_0.back(), z_0.back());
        double fz1 = fz(x_0.back(), y_0.back(), z_0.back());

        double fx2 = fx(x_0.back() + fx1 * dt / 2.0, y_0.back() + fy1 * dt / 2.0, z_0.back() + fz1 * dt / 2.0);
        double fy2 = fy(x_0.back() + fx1 * dt / 2.0, y_0.back() + fy1 * dt / 2.0, z_0.back() + fz1 * dt / 2.0);
        double fz2 = fz(x_0.back() + fx1 * dt / 2.0, y_0.back() + fy1 * dt / 2.0, z_0.back() + fz1 * dt / 2.0);

        double fx3 = fx(x_0.back() + fx2 * dt / 2.0, y_0.back() + fy2 * dt / 2.0, z_0.back() + fz2 * dt / 2.0);
        double fy3 = fy(x_0.back() + fx2 * dt / 2.0, y_0.back() + fy2 * dt / 2.0, z_0.back() + fz2 * dt / 2.0);
        double fz3 = fz(x_0.back() + fx2 * dt / 2.0, y_0.back() + fy2 * dt / 2.0, z_0.back() + fz2 * dt / 2.0);

        double fx4 = fx(x_0.back() + fx3 * dt, y_0.back() + fy3 * dt, z_0.back() + fz3 * dt);
        double fy4 = fy(x_0.back() + fx3 * dt, y_0.back() + fy3 * dt, z_0.back() + fz3 * dt);
        double fz4 = fz(x_0.back() + fx3 * dt, y_0.back() + fy3 * dt, z_0.back() + fz3 * dt);

        x_0.push_back(x_0.back() + (fx1 + 2 * fx2 + 2 * fx3 + fx4) * dt / 6.0);
        y_0.push_back(y_0.back() + (fy1 + 2 * fy2 + 2 * fy3 + fy4) * dt / 6.0);
        z_0.push_back(z_0.back() + (fz1 + 2 * fz2 + 2 * fz3 + fz4) * dt / 6.0);
    }
}

double delta_n(
    double x_0_, double y_0_, double z_0_,
    double x, double y, double z
) {
    return sqrt(
        (x_0_ - x) * (x_0_ - x) +
        (y_0_ - y) * (y_0_ - y) +
        (z_0_ - z) * (z_0_ - z));
}

void runge_kutta(
    double (*fx)(double , double, double),
    double (*fy)(double , double, double),
    double (*fz)(double , double, double),
    double x,
    double y,
    double z,
    double dt,
    double start,
    double end,
    const std::string path
) {
    std::ofstream file;
    file.open(path, std::ios::out);
    std::vector<double>::iterator x_0it = x_0.begin(), y_0it = y_0.begin(), z_0it = z_0.begin();

    double t;
    for (t = start; t < end; t += dt) {
        file<<t<<" "<<delta_n(*x_0it, *y_0it, *z_0it, x, y, z)<<std::endl;
        x_0it = std::next(x_0it);
        y_0it = std::next(y_0it);
        z_0it = std::next(z_0it);

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
    
    file<<t<<" "<<delta_n(*x_0it, *y_0it, *z_0it, x, y, z)<<std::endl;
    file.close();
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
    const double start = 0, end = 100, dt = 0.01;
    x_0.push_back(1);
    y_0.push_back(0);
    z_0.push_back(0);
    runge_kutta_0(fx, fy, fz, dt, start, end);

    for (int n = 2; n <= 6; n += 2) {
        const std::string path = "laurents" + std::to_string(n) + ".txt";
        const double epsilon = pow(10, -n);
        const double x = 1 + epsilon, y = 0, z = 0;
        runge_kutta(fx, fy, fz, x, y, z, dt, start, end, path);
    }
}