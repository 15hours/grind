#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        int n; std::cin >> n;
        int cnt[101] = {0};
        int a[n];
        int b[n];
        bool conditionPlaced[101] = {false};
        for (int i = 0; i < n; i++) {
            std::cin >> a[i];
            cnt[a[i]]++;
        }

        int possible = 0;
        for (int num : cnt) {
            if (num >= 2) {
                possible++;
            }
        }
        if (possible < 2) {
            std::cout << -1 <<'\n';
        } else {
            int rightOfFirst = 0;
            for (int i = 0; i < n; i++) {
                if (cnt[a[i]] == 1) {
                    b[i] = 1;
                } else {
                    if (rightOfFirst == 0 || rightOfFirst == a[i]) {
                        if (conditionPlaced[a[i]] == false) {
                            conditionPlaced[a[i]] = true;
                            b[i] = 1;
                            rightOfFirst = a[i];
                        } else {
                            b[i] = 2;
                        }
                    } else {
                        if (conditionPlaced[a[i]] == false) {
                            conditionPlaced[a[i]] = true;
                            b[i] = 2;
                        } else {
                            b[i] = 3;
                        }
                    }
                }
                std::cout << b[i] << " ";
            }
            std::cout << '\n';
        }
    }
}
