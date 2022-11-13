#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>

#include "solver.h"


class CrankSolverWithDirichletCondition: Solver {
private:
    double c, uL, uR;

    void set_condition_values() override {
        Solver::u[0] = this->uL;
        Solver::u[Solver::N + 1] = this->uR;
    }

    const std::vector<std::vector<double>> calculate_A() {
        std::vector<std::vector<double>> A(Solver::N + 2, std::vector<double>(Solver::N + 2, 0));
        for (int i = 1; i <= Solver::N; i++) {
            A[i][i - 1] = -this->c / 2.0;
            A[i][i] = 1 + this->c;
            A[i][i + 1] = -this->c / 2.0;
        }

        return A;
    }

    const std::pair<std::vector<double>, std::vector<double>> LU_decomposition(
        const std::vector<std::vector<double>> A
    ) {
        std::vector<double> alpha(N + 1, 0), beta(N + 1, 0);
        for (int i = 1; i <= Solver::N; i++) {
            alpha[i] = A[i][i] - A[i][i - 1] * beta[i - 1];
            beta[i] = A[i][i + 1] / alpha[i];
        }

        return std::make_pair(alpha, beta);
    }

    const std::vector<double> calculate_z(
        const std::vector<double> alpha,
        const std::vector<double> beta
    ) {
        std::vector<double> z(N + 1);
        z[1] = (1 - this->c) * Solver::u[1] + this->c * this->uL + this->c / 2.0 * Solver::u[2];
        for (int i = 2; i <= Solver::N - 1; i++) {
            z[i] = (1 - this->c) * Solver::u[i] + this->c / 2.0 * (Solver::u[i - 1] + Solver::u[i + 1]);
        }
        z[N] = (1 - this->c) * Solver::u[N] + this->c * this->uR + this->c / 2.0 * Solver::u[N - 1];

        return z;
    }

    const std::vector<double> calculate_y(
        const std::vector<double> alpha,
        const std::vector<std::vector<double>> A,
        const std::vector<double> z
    ) {
        std::vector<double> y(N + 1, 0);
        for (int i = 1; i <= Solver::N; i++) {
            y[i] = (z[i] - A[i][i - 1] * y[i - 1]) / alpha[i];
        }

        return y;
    }

    const std::vector<double> calculate_x(
        const std::vector<double> beta,
        const std::vector<double> y
    ) {
        std::vector<double> x(N + 2, 0);
        for (int i = N; i >= 1; i--) {
            x[i] = y[i] - beta[i] * x[i + 1];
        }

        return x;
    }

public:
    CrankSolverWithDirichletCondition(
        const double dt,
        const double dx,
        const double N,

        const double (*u0)(const double),
        const double uL,
        const double uR
    ): Solver(dt, dx, N) {
        c = Solver::dt / Solver::dx / Solver::dx;

        this->uL = uL;
        this->uR = uR;

        this->set_initial_values(u0);
    }

    void solve(const double t_end) override {
        const std::vector<std::vector<double>> A = this->calculate_A();

        std::vector<double> alpha, beta;
        std::tie(alpha, beta) = this->LU_decomposition(A);

        for (int n = 1; n * Solver::dt <= t_end; n++) {
            const std::vector<double> z = this->calculate_z(alpha, beta);
            const std::vector<double> y = this->calculate_y(alpha, A, z);
            const std::vector<double> x = this->calculate_x(beta, y);

            for (int i = 1; i <= N; i++) {
                Solver::u[i] = x[i];
            }

            this->set_condition_values();
            
            Solver::print_u(n * Solver::dt);
        }
    }
};


const double u0(const double x) {
    return 1.0 / sqrt(2.0 * M_PI) * exp(-(x - 5.0) * (x - 5.0) / 2.0);
}


int main() {
    std::cout << std::fixed << std::setprecision(16);

    CrankSolverWithDirichletCondition solver = CrankSolverWithDirichletCondition(0.01, 0.05, 200, u0, 0, 0);
    solver.solve(5);
}