#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
#include <iterator>


class SchroedingerSolver {
private:
    double dt, dx, N;
    std::vector<double> R, I;

    void set_condition_values() {
        this->R[0] = this->R[this->N];
        this->R[this->N + 1] = this->R[1];
        this->I[0] = this->I[this->N];
        this->I[this->N + 1] = this->I[1];
    }

    void set_initial_values(
        const double (*psi0)(const double)
    ) {
        for (int i = 1; i <= this->N; i++) {
            this->R[i] = (psi0((i - 1) * this->dx - this->N * this->dx / 2.0) + psi0(i * this->dx - this->N * this->dx / 2.0)) / 2.0;
            const double xi = (i - 1.0 / 2.0) * this->dx - this->N * this->dx / 2.0;
            this->I[i] = -this->dt * (-(this->R[i - 1] - 2.0 * this->R[i] + this->R[i + 1]) / this->dx / this->dx + xi * xi * this->R[i]) / 2.0;
        }
        this->set_condition_values();
    }

    void print_RI(
        const double t,
        const std::vector<double> I_
    ) {
        std::cout << t;
        for (int i = 0; i <= this->N + 1; i++) {
            std::cout << " " << this->R[i] * this->R[i] + this->I[i] * I_[i];
        }
        std::cout << std::endl;
    }

public:
    SchroedingerSolver(
        const double dt,
        const double dx,
        const int N,

        const double (*psi0)(const double)
    ): R(N + 2, 0), I(N + 2, 0) {
        this->dt = dt;
        this->dx = dx;
        this->N = N;

        this->set_initial_values(psi0);
    }

    void solve(
        const double t_end
    ) {
        for (int n = 1; n * this->dt <= t_end; n++) {
            for (int i = 1; i <= this->N; i++) {
                const double xi = (i - 1.0 / 2.0) * this->dx - this->N * this->dx / 2.0;
                this->R[i] += this->dt * (-(this->I[i - 1] - 2.0 * this->I[i] + this->I[i + 1]) / this->dx / this->dx + xi * xi * this->I[i]) / 2.0;
            }

            std::vector<double> I_;
            std::copy(this->I.begin(), this->I.end(), std::back_inserter(I_));
            for (int i = 1; i <= this->N; i++) {
                const double xi = (i - 1.0 / 2.0) * this->dx - this->N * this->dx / 2.0;
                this->I[i] -= this->dt * (-(this->R[i - 1] - 2.0 * this->R[i] + this->R[i + 1]) / this->dx / this->dx + xi * xi * this->R[i]) / 2.0;
            }

            this->set_condition_values();
            
            this->print_RI(n * this->dt, I_);
        }
    }
};


const double psi0(
    const double x
) {
    return sqrt(2.0) * exp(-2.0 * (x - 5.0) * (x - 5.0)) / pow(M_PI, 1.0 / 4.0);
}


int main() {
    std::cout << std::fixed << std::setprecision(16);

    SchroedingerSolver solver = SchroedingerSolver(0.001, 0.05, 400, psi0);
    solver.solve(8);
}