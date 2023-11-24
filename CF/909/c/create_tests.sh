#!/bin/bash

# Create folder
folder="tests_data"

rm -rf "$folder"
mkdir -p "$folder"
echo "Folder created: $folder"

# Create test cases
input_1="tests_data/input_1.txt"
expected_1="tests_data/expected_1.txt"

input_2="tests_data/input_2.txt"
expected_2="tests_data/expected_2.txt"

cat <<EOF > "$input_1"
7
5
1 2 3 4 5
4
9 9 8 8
6
-1 4 -1 0 5 -4
4
-1 2 4 -3
1
-1000
3
101 -99 101
20
-10 5 -8 10 6 -10 7 9 -2 -6 7 2 -4 6 -1 7 -6 -7 4 1
EOF

cat <<EOF > "$expected_1"
15
17
8
4
-1000
101
10
EOF

