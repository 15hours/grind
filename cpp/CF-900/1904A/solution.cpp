#include <iostream>

int main() {
    int t; std::cin >> t;

    while (t--) {
        int a, b; std::cin >> a >> b;
        int xk, yk; std::cin >> xk >> yk;
        int xq, yq; std::cin >> xq >> yq;

        int count = 0;

        int dir[4][2] = {{-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
        for (int i = 0; i < 4; i++) {
            int x1 = dir[i][0]*a + xk;
            int y1 = dir[i][1]*b + yk;
            int q1 = dir[i][0]*b + xk;
            int p1 = dir[i][1]*a + yk;

            for (int j = 0; j < 4; j++) {
                int x2 = dir[j][0]*a + xq;
                int y2 = dir[j][1]*b + yq;
                int q2 = dir[j][0]*b + xq;
                int p2 = dir[j][1]*a + yq;

                if (x1 == x2 && y1 == y2 || x1 == q2 && y1 == p2) {
                    count++;
                }
                if (q1 == x2 && p1 == y2 || q1 == q2 && p1 == p2) {
                    count++;
                }

            }
        }
        if (a == b) {
            std::cout << count / 2 << '\n';
        } else {
            std::cout << count << '\n';
        }
    }
}
