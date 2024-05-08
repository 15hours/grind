#include <algorithm>
#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        long long a, b, c; std::cin >> a >> b >> c;
        if (a == b && b == c) {
            std::cout << "Yes" << '\n';
            continue;
        }

        int minNum = std::min(a, std::min(b, c));
        int maxNum = std::max(a, std::max(b, c));
        int midNum = a + b + c - minNum - maxNum;

        if (maxNum % minNum != 0 || midNum % minNum != 0) {
            std::cout << "No" << '\n';
            continue;
        }

        if (minNum == midNum && maxNum / minNum <= 4) {
            std::cout << "Yes" << '\n';
            continue;
        }

        if (maxNum / minNum <= 3 && midNum / minNum == 2) {
            std::cout << "Yes" << '\n';
            continue;
        }

        std::cout << "No" << '\n';
    }
}
