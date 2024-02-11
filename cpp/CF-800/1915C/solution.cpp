#include <cmath>
#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n; std::cin >> n;
        int a[n];
        long long sum = 0;
        for (int i = 0; i < n; i++) {
            std::cin >> a[i];
            sum += a[i];
        }

        long long sr = sqrt(sum);
        if (sr * sr == sum) {
            std::cout << "yes" << "\n";
        } else {
            std::cout << "no" << "\n";
        }
    }
}
