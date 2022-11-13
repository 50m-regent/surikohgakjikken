#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
#include <iterator>

#include "solver.h"


double b;


class EulerSolverWithDirichletCondition: Solver {
private:
    double uL, uR;

    void set_condition_values() override {
        Solver::u[0] = this->uL;
        Solver::u[Solver::N + 1] = this->uR;
    }

public:
    EulerSolverWithDirichletCondition(
        const double dt,
        const double dx,
        const double N,

        const double (*u0)(const double),
        const double uL,
        const double uR
    ): Solver(dt, dx, N) {
        this->uL = uL;
        this->uR = uR;

        this->set_initial_values(u0);
    }

    void solve(const double t_end) override {
        for (int n = 1; n * Solver::dt <= t_end; n++) {
            std::vector<double> u_;
            std::copy(Solver::u.begin(), Solver::u.end(), std::back_inserter(u_));

            for (int i = 1; i <= Solver::N; i++) {
                Solver::u[i] += Solver::dt * (u_[i] * (1 - u_[i]) + (u_[i - 1] - 2 * u_[i] + u_[i + 1]) / Solver::dx / Solver::dx);
            }
            this->set_condition_values();
            
            Solver::print_u(n * Solver::dt);
        }
    }
};


const double u0(const double x) {
    return 1.0 / (1.0 + exp(b * x - 5.0)) / (1.0 + exp(b * x - 5.0));
}


int main(const int argc, const char *argv[]) {
    if (argc != 2) {
        return EXIT_FAILURE;
    }
    b = atof(argv[1]);
    
    std::cout << std::fixed << std::setprecision(16);

    EulerSolverWithDirichletCondition solver = EulerSolverWithDirichletCondition(0.001, 0.05, 4000, u0, 1, 0);
    solver.solve(40);
}