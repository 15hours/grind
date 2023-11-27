#!/bin/bash

# Create folder
folder="tests_data"

rm -rf "$folder"
mkdir -p "$folder"
echo "Folder created: $folder"

# Create test cases
input_1="tests_data/input_1.txt"
expected_1="tests_data/expected_1.txt"

cat <<EOF > "$input_1"
5
3
...
7
##....#
7
..#.#..
4
####
10
#...#..#.#
EOF

cat <<EOF > "$expected_1"
2
2
5
0
2
EOF
