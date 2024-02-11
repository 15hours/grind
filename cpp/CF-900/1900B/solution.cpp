#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int a, b, c; std::cin >> a >> b >> c;
        std::cout << (b+c+1)%2 << " " << (a+c+1)%2 << " "<< (a+b+1)%2 << '\n';
    }
}
