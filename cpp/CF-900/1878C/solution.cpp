#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;

    while (t--) {
        long long n, k, x; std::cin >> n >> k >> x;

        long long minSum = 0, maxSum = 0;
        for (int i = 0; i < k; i++) {
            minSum += i + 1;
            maxSum += n - i;
        }

        if (minSum <= x && x <= maxSum) {
            std::cout << "Yes" << '\n';
        } else {
            std::cout << "No" << '\n';
        }
    }
}
