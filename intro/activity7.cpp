#include <iostream>
#include <vector>

void sanitize(std::vector<bool>& flags, int n, int N) {
    for (int i = 2 * n; i <= N; i += n) {
        flags[i] = false;
    }
}

int main(int argc, char **argv) {
    if (argc != 2) {
        return EXIT_FAILURE;
    }

    int N = atoi(argv[1]);
    std::vector<bool> is_i_prime(N + 1, true);

    is_i_prime[1] = false;

    for (int i = 2; i <= N; i++) {
        if (!is_i_prime[i]) {
            continue;
        }
        
        std::cout << i << std::endl;
        sanitize(is_i_prime, i, N);
    }

    return EXIT_SUCCESS;
}
