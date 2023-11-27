t = int(input())

for _ in range(t):
    n = int(input())
    s = [c for c in input()]

    empty_cell_count = 0
    actions_count = 0

    for i in range(n):
        if s[i] == '.':
            empty_cell_count += 1

        if empty_cell_count >= 3:
            actions_count = 2
            break

        if s[i] == '#' or i == n - 1:
            if empty_cell_count == 0:
                continue

            actions_count += empty_cell_count
            empty_cell_count = 0

    print(actions_count)
