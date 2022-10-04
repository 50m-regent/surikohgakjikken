#include <iostream>
#include <vector>

double f(std::vector<double>& x) {
    double sum = 0;
    for (double& xx: x) {
        sum += xx += 1;
        
    }
    return sum / x.size();
}

int main() {
    std::vector<double> x(10);
    for (double& xx: x) {
        xx = 0.3;
    }
    std::cout<<f(x)<<std::endl;
    return EXIT_SUCCESS;
}
