num_inputs = int(input())

for _ in range(num_inputs):
    x = int(input())

    if x % 3 == 0:
        print("Second")
    else:
        print("First")
