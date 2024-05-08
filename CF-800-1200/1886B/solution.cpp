#include <cmath>
#include <iostream>

double distance(double x1, double y1, double x2, double y2) {
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

void solve() {
    double px, py; std::cin >> px >> py;
    double ax, ay; std::cin >> ax >> ay;
    double bx, by; std::cin >> bx >> by;

}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t; std::cin >> t;
    while (t--) {
        solve();
    }
}
