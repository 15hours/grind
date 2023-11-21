t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    max_diff = 0
    max_k = int(n / 2)
    for k in range(1, max_k + 1):
        if n % k != 0:
            continue

        boxes = [0] * int(n / k)
        j = 0
        for i in range(n):
            boxes[j] += a[i]
            if (i + 1) % k == 0:
                j += 1

        max_diff = max(max_diff, max(boxes) - min(boxes))

    print(max_diff)
