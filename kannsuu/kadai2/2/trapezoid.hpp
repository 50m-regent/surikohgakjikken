const double trapezoid(
    const double (*f)(const double),
    const double start,
    const double end,
    const int n
) {
    const double h = (end - start) / (double)n;
    double return_value = 0;
    for (double x = start + h; x < end; x += h) {
        return_value += 2.0 * f(x);
    }

    return (f(start) + return_value + f(end)) * h / 2.0;
}