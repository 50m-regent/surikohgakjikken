#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
#include <iterator>

#include "solver.h"


class EulerSolverWithNeumannCondition: Solver {
private:
    double JL, JR;

    void set_condition_values() override {
        Solver::u[0] = Solver::u[1] - this->JL * Solver::dx;
        Solver::u[Solver::N + 1] = Solver::u[Solver::N] + this->JR * Solver::dx;
    }

public:
    EulerSolverWithNeumannCondition(
        const double dt,
        const double dx,
        const double N,

        const double (*u0)(const double),
        const double JL,
        const double JR
    ): Solver(dt, dx, N) {
        this->JL = JL;
        this->JR = JR;

        this->set_initial_values(u0);
    }

    void solve(const double t_end) override {
        for (int n = 1; n * Solver::dt <= t_end; n++) {
            std::vector<double> u_;
            std::copy(Solver::u.begin(), Solver::u.end(), std::back_inserter(u_));

            for (int i = 1; i <= Solver::N; i++) {
                Solver::u[i] += (u_[i - 1] - 2 * u_[i] + u_[i + 1]) * Solver::dt / Solver::dx / Solver::dx;
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

    EulerSolverWithNeumannCondition solver = EulerSolverWithNeumannCondition(0.01, 0.5, 20, u0, 0, 0);
    solver.solve(5);
}