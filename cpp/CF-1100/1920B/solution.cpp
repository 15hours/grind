#include <algorithm>
#include <iostream>


void solve() {
    int n, k, x;
    std::cin >> n >> k >> x;

    int a[n];
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::sort(a, a + n, std::greater<int>());

    long long bobSum = 0, aliceSum = 0;
    for (int i = 0; i < x; i++) {
        bobSum += a[i];
    }
    for (int i = x; i < n; i++) {
        aliceSum += a[i];
    }

    int maxSum = aliceSum - bobSum;
    int kCount = k;
    int i = 0;
    while (kCount > 0) {
        bobSum -= a[i];
        if (x + i < n) {
            bobSum += a[x + i];
            aliceSum -= a[x + i];
        }
        kCount--;
        i++;

        if (aliceSum - bobSum > maxSum) {
            int curSum = aliceSum - bobSum;
            if (curSum > maxSum) {
                maxSum = curSum;
            }
        }
    }

    std::cout << maxSum << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t;
    std::cin >> t;
    while (t--) {
        solve();
    }
}
