t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    max_between = 0
    for i in range(1, len(a)):
        max_between = max(max_between, a[i] - a[i - 1])

    print(max(a[0], 2 * (x - a[n - 1]), max_between))
