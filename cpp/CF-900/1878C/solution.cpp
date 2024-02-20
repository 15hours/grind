#include <iostream>
// #include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    // std::vector<long long> sums(2*1E5);
    // sums[0] = 0;
    // for (int i = 1; i <= 2*1E5; i++) {
    //     sums[i] += sums[i - 1] + i;
    // }

    int t; std::cin >> t;

    while (t--) {
        long long n, k, x; std::cin >> n >> k >> x;
        long long minSum = k*(k + 1)/2;
        long long maxSum = n*(n + 1)/2 - (n - k)*(n - k + 1)/2;

        if (minSum <= x && x <= maxSum) {
        // if (sums[k] <= x && x <= sums[n] - sums[n - k]) {
            std::cout << "Yes" << '\n';
        } else {
            std::cout << "No" << '\n';
        }
    }
}
