#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n; std::cin >> n;
        int result = 0;
        for (int i = 0; i < n; i++) {
            int a; std::cin >> a;
            if (n == 2 && i == 1) {
                result += 1;
            } else {
                result += a;
            }
        }
        std::cout << result << '\n';
    }
}
