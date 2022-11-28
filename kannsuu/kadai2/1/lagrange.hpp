#include <iostream>
#include <vector>

class Lagrange {
private:
    const double (*f)(const double);
    const double start, end;
    const int n;

    std::vector<double> xs;

    void calculate_points() {
        for (int i = 0; i <= this->n; i++) {
            this->xs[i] = this->start + (this->end - this->start) / (double)n * (double)i;
        }
    }

    const double l(
        const int i,
        const double x
    ) {
        double return_value = 1;
        for (int j = 0; j <= this->n; j++) {
            if (j == i) {
                continue;
            }

            return_value *= (x - this->xs[j]) / (this->xs[i] - this->xs[j]);
        }

        return return_value;
    }

    const double P(const double x) {
        double return_value = 0;
        for (int i = 0; i <= this->n; i++) {
            return_value += f(this->xs[i]) * this->l(i, x);
        }

        return return_value;
    }

public:
    Lagrange(
        const double (*f)(const double),
        const double start,
        const double end,
        const int n
    ) : f(f), start(start), end(end), n(n), xs(n + 1, 0) {
        this->calculate_points();
    }

    void print_interpolated(
        const double dx
    ) {
        for (double x = this->start; x <= this->end; x += dx) {
            std::cout << x << " " << this->P(x) << std::endl;
        }
    }
};