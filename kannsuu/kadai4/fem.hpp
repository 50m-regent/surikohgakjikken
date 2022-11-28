#include <vector>
#include <cmath>
#include <iostream>

#include "gauss.hpp"

class GaussJordan {
private:
    std::vector<std::vector<double>> A;
    std::vector<double> b;
    std::vector<double> x;

    const int get_pivot(const int i) {
        int pivot = i;
        for (int j = i + 1; j < A.size(); j++) {
            if (abs(A[pivot][i]) < abs(A[j][i])) {
                pivot = j;
            }
        }

        return pivot;
    }

    const void up2down() {
        for (int i = 0; i < this->A[0].size() - 1; i++) {
            const int pivot = this->get_pivot(i);
            std::iter_swap(this->A.begin() + i, this->A.begin() + pivot);
            std::iter_swap(this->b.begin() + i, this->b.begin() + pivot);

            for (int j = i + 1; j < this->A.size(); j++) {
                this->b[j] -= this->b[i] * this->A[j][i] / this->A[i][i];
                for (int k = this->A[0].size() - 1; k >= i; k--) {
                    this->A[j][k] -= this->A[i][k] * this->A[j][i] / this->A[i][i];
                }
            }
        }
    }

    const void down2up() {
        for (int i = this->A.size() - 1; i >= 0; i--) {
            this->x[i] = this->b[i];
            for (int j = i + 1; j < this->A[0].size(); j++) {
                this->x[i] -= this->A[i][j] * this->x[j];
            }
            this->x[i] /= this->A[i][i];
        }
    }

public:
    GaussJordan(
        const std::vector<std::vector<double>> A,
        const std::vector<double> b
    ) : A(A), b(b), x(b.size()) {
        this->up2down();
        this->down2up();
    }

    const std::vector<double> get_x() {
        return this->x;
    }
};

class TGenerator {
private:
    //const double x_previous, x_now, x_next, h;
public:
const double x_previous, x_now, x_next, h;
    TGenerator(
        const double x_previous,
        const double x_now,
        const double x_next,
        const double h
    ) : x_previous(x_previous), x_now(x_now), x_next(x_next), h(h) {
    }

    const double t(const double x) const {
        if (this->x_previous <= x && x < this->x_now) {
            return (x - this->x_previous) / this->h;
        } else if (this->x_now <= x && x < x_next) {
            return (this->x_next - x) / this->h;
        } else {
            return 0;
        }
    }

    const double dt(const double x) const {
        if (this->x_previous <= x && x < this->x_now) {
            return 1.0 / this->h;
        } else if (this->x_now <= x && x < x_next) {
            return -1.0 / this->h;
        } else {
            return 0;
        }
    }
};

class FEM {
private:
    const double start, end;
    const int n;
    const int M = 3;
    const std::vector<double> y{-sqrt(3.0 / 5.0), 0, sqrt(3.0 / 5.0)};
    const std::vector<double> w{5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0};

    std::vector<TGenerator> t;
    std::vector<double> c;

    void calculate_t(
        const double start,
        const double end,
        const int n
    ) {
        const double h = (end - start) / (double)n;
        double x = start + h;
        for (int i = 0; i < n - 1; i++, x += h) {
            this->t.push_back(TGenerator(x - h, x, x + h, h));
        }
    }

    const std::vector<std::vector<double>> calculate_A(
        const double start,
        const double end,
        const int n,
        const double (*p)(const double),
        const double (*q)(const double)
    ) {
        std::vector<std::vector<double>> A(n - 1, std::vector<double>(n - 1));
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                std::function<double(double)> f = [&](const double x) {
                    return p(x) * t[i].dt(x) * t[j].dt(x) + q(x) * t[i].t(x) * t[j].t(x);
                };
                A[i][j] = gauss(f, start, end, 1000, M, y, w);
            }
        }

        return A;
    }

    const std::vector<double> calculate_b(
        const double start,
        const double end,
        const int n,
        const double (*f)(const double)
    ) {
        std::vector<double> b(n - 1);
        for (int i = 0; i < n - 1; i++) {
            const std::function<double(double)> ff = [&](const double x) {
                return f(x) * t[i].t(x);
            };
            
            b[i] = gauss(ff, start, end, 1000, M, y, w);
        }

        return b;
    }

public:
    FEM(
        const double start,
        const double end,
        const int n,
        const double (*p)(const double),
        const double (*q)(const double),
        const double (*f)(const double)
    ) : start(start), end(end), n(n) {
        this->calculate_t(start, end, n);

        const std::vector<std::vector<double>> A = this->calculate_A(start, end, n, p, q);
        
        const std::vector<double> b = this->calculate_b(start, end, n, f);
        this->c = GaussJordan(A, b).get_x();
    }

    const std::vector<double> get_u(const std::vector<double> x) const {
        std::vector<double> u;
        const double h = (this->end - this->start) / this->n;
        for (const double xx: x) {
            double uu = 0;
            for (int j = 0; j < this->n - 1; j++) {
                uu += this->c[j] * this->t[j].t(xx);
            }
            u.push_back(uu);
        }

        return u;
    }
};