#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n, k; std::cin >> n >> k;
        int b[n];

        long long p = 1;
        for (int i = 0; i < n; i++) {
            std::cin >> b[i];
            p *= b[i];
        }

        if (2023 % p != 0) {
            std::cout << "No" << "\n";
            continue;
        }

        std::cout << "Yes" << "\n";
        std::cout << 2023 / p;
        for (int i = 0; i < k - 1; i++) {
            std::cout << " 1";
        }
        std::cout << "\n";
    }
}
