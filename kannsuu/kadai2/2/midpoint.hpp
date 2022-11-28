const double midpoint(
    const double (*f)(const double),
    const double start,
    const double end,
    const int n
) {
    const double h = (end - start) / (double)n;
    double lastx = start;
    double return_value = 0;
    for (double x = lastx + h; x <= end; lastx = x, x += h) {
        return_value += f((lastx + x) / 2.0);
    }

    return return_value * h;
}