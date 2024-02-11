#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;

    while (t--) {
        int n; std::cin >> n;

        long long aSum = 0;
        int aMin = 1E9;
        for (int i = 0; i < n; i++) {
            int a; std::cin >> a;
            aSum += a;
            aMin = std::min(aMin, a);
        }

        long long bSum = 0;
        int bMin = 1E9;
        for (int i = 0; i < n; i++) {
            int b; std::cin >> b;
            bSum += b;
            bMin = std::min(bMin, b);
        }

        std::cout << std::min(aSum + 1LL * n * bMin, bSum + 1LL * n * aMin) << '\n';
    }
}
