#include <iostream>
#include <string>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n; std::cin >> n;
        std::string s; std::cin >> s;

        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += (s[i] == '+') ? 1 : -1;
        }

        std::cout << abs(sum) << std::endl;
    }
}
