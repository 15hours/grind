#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int n; std::cin >> n;
        char s[n];
        int count = 0, tmpCount = 0;
        for (int i = 0; i < n; i++) {
            std::cin >> s[i];
            if (s[i] == 'B') {
                if (tmpCount == 0) {
                    continue;
                } else {
                    count += tmpCount;
                    tmpCount = 1;
                }
            } else {
                tmpCount++;
            }
        }

        std::cout << count << '\n';
    }
}
