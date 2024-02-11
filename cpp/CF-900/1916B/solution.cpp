#include <iostream>
#include <numeric>

int main() {
    int t; std::cin >> t;

    while (t--) {
        long long a, b; std::cin >> a >> b;

        if (b % a == 0) {
            std::cout << b * (b / a) << '\n';
        } else {
            std::cout << (a * b) / std::gcd(a, b) << '\n';
        }
    }
}
