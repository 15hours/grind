t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    subarr_start = 0
    subarr_end = 0

    greates_sum = a[0]
    for i in range(1, n):
        if a[i] % 2 == a[i - 1] % 2:
            subarr_end = i

            cur_sum = 0
            max_sum = -10000

            for j in range(subarr_start, subarr_end):
                cur_sum += a[j]
                if cur_sum > max_sum:
                    max_sum = cur_sum
                if cur_sum < 0:
                    cur_sum = 0

            greates_sum = max(greates_sum, max_sum)
            subarr_start = i
        elif i == n - 1:
            subarr_end = n

            cur_sum = 0
            max_sum = -10000

            for j in range(subarr_start, subarr_end):
                cur_sum += a[j]
                if cur_sum > max_sum:
                    max_sum = cur_sum

                if cur_sum < 0:
                    cur_sum = 0

            greates_sum = max(greates_sum, max_sum)

    print(greates_sum)
