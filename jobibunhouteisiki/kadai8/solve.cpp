#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>

double runge_kutta(
    double (*f)(double, int, double, int, double, double),
    std::vector<double> x,
    double K,
    int N,
    double dt,
    double start,
    double end
) {
    double t;
    double Rx, Ry;
    double Rsum = 0;
    for (t = start; t < end; t += dt) {
        Rx = Ry = 0;
        for (int i = 0; i < N; i++) {
            Rx += cos(x[i]) / N;
            Ry += sin(x[i]) / N;
        }

        for (int i = 0; i < N; i++) {
            double f1 = f(x[i], i, K, N, Rx, Ry);
            double f2 = f(x[i] + f1 * dt / 2.0, i, K, N, Rx, Ry);
            double f3 = f(x[i] + f2 * dt / 2.0, i, K, N, Rx, Ry);
            double f4 = f(x[i] + f3 * dt, i, K, N, Rx, Ry);

            x[i] += (f1 + 2 * f2 + 2 * f3 + f4) * dt / 6.0;
        }

        Rsum += sqrt(Rx * Rx + Ry * Ry) * dt;
    }

    return Rsum / (end - start);
}

double omega(int i, int N) {
    return tan(M_PI * ((double)(i + 1) / (N + 1) - 0.5));
}

double f(double x, int i, double K, int N, double Rx, double Ry) {
    return omega(i, N) - K * (sin(x) * Rx - cos(x) * Ry);
}

void calculate_Rs(int N) {
    std::cout<<std::fixed<<std::setprecision(16);

    const double start = 50, end = 100, dt = 0.01;
    std::vector<double> x(N);
    for (int i = 0; i < N; i++) {
        double y = 2 * M_PI / N * (i - 1);
        x[i] = y + 0.01 * sin(y);
    }

    for (double K = 1; K <= 3 + 1e-7; K += 0.1) {
        const double R = runge_kutta(f, x, K, N, dt, start, end);
        std::cout<<K<<" "<<R<<std::endl;
    }
}

int main(int argc, char *argv[]) {
    if (2 != argc) {
        return 1;
    }

    const int N = atoi(argv[1]);
    calculate_Rs(N);
}