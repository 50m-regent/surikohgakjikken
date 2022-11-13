#include <iostream>
#include <vector>

class Solver {
protected:
    double dt, dx;
    int N;

    std::vector<double> u;

    void print_u(const double t) {
        std::cout << t;
        for (int i = 0; i <= this->N + 1; i++) {
            std::cout << " " << this->u[i];
        }
        std::cout << std::endl;
    }

    void set_initial_values(
        const double (*u0)(const double)
    ) {
        for (int i = 1; i <= Solver::N; i++) {
            Solver::u[i] = (u0((i - 1) * Solver::dx) + u0(i * Solver::dx)) / 2.0;
        }
        this->set_condition_values();

        this->print_u(0);
    }

    virtual void set_condition_values() = 0;

public:
    Solver(
        const double dt,
        const double dx,
        const int N
    ): u(N + 2) {
        this->dt = dt;
        this->dx = dx;
        this->N = N;
    }

    virtual ~Solver() {}

    virtual void solve(
        const double t_end
    ) = 0;
};