#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n, l, r, k; std::cin >> n >> l >> r >> k;
        int a[n + 1];
        a[0] = 0;

        int answer = -1;
        if (l <= k && k <= r) {
            answer = 0;
        }

        for (int i = 1; i < n + 1; i++) {
            std::cin >> a[i];
            if (answer != -1) {
                continue;
            }
            if (k < l) {
                k += (a[i]-a[i-1]);
            } else if (k > r) {
                k -= (a[i]-a[i-1]);
            }

            if (l <= k && k <= r) {
                answer = a[i];
            }

        }

        std::cout << answer << '\n';
    }
}
