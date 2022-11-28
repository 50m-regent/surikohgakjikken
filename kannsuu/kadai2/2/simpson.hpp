const double simpson(
    const double (*f)(const double),
    const double start,
    const double end,
    const int n
) {
    const double h = (end - start) / (double)n;
    double return_value = f(start) + f(end);
    double lastx = start;
    for (double x = start + h; x <= end; lastx = x, x += h) {
        return_value += 2.0 * f(lastx) + 4 * f((lastx + x) / 2.0);
    }

    return return_value * h / 6.0;
}