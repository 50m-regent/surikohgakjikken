#include <vector>

const double gauss(
    const std::function<double(double)> f,
    const double start,
    const double end,
    const int n,
    const int M,
    const std::vector<double> y,
    const std::vector<double> w
) {
    /*
    const double h = (end - start) / (double)n;
    double return_value = 0;
    for (double x = start + h; x <= end; x += h) {
        for (int m = 0; m < M; m++) {
            return_value += w[m] * f((y[m] + 1.0) * h / 2.0 + x) * h / 2.0;
        }
    }

    return return_value;
    */
    
    
    const double h = (end - start) / (double)n;
    double return_value = 0;
    for (double x = start + h; x < end; x += h) {
        return_value += 2.0 * f(x);
    }

    return (f(start) + return_value + f(end)) * h / 2.0;
}