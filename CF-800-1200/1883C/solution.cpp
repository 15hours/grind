#include <ios>
#include <iostream>

void solve() {
    int n, k; std::cin >> n >> k;
    int cnt = -1;
    int a[n];
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];

        if (k == 2 && a[i] % 2 == 0) {
            cnt = 0;
        } else if (k == 3 && a[i] % 3 == 0) {
            cnt = 0;
        } else if (k == 4 && a[i] % 4 == 0) {
            cnt = 0;
        } else if (k == 5 && a[i] % 5 == 0) {
            cnt = 0;
        }
    }
    int numOps = 0;

    if (cnt == 0) {
        std::cout << 0 << '\n';
        return;
    } else if (k == 2) {
        numOps = 1;
    } else if (k == 3) {
        for (int& x : a) {
            if (x % 3 == 2) {
                numOps = 1;
                break;
            }
        }
        if (numOps == 0) {
            numOps = 2;
        }
    } else if (k == 5) {
        int minOps = 4;
        for (int& x : a) {
            if (5 - x % 5 < minOps) {
                minOps = 5 - x % 5;
            }
        }
        numOps = minOps;
    } else {
        int countTwos = 0;
        for (int& x : a) {
            if (x % 2 == 0) {
                countTwos++;
            }
            if (x % 4 == 3) {
                numOps = 1;
            }
            if (countTwos >= 2) {
                numOps = 0;
                break;
            }
        }
        if (countTwos == 1) {
            numOps = 1;
        } else if (countTwos == 0 && numOps != 1) {
            numOps = 2;
        }
    }
    std::cout << numOps << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
