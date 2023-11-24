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
6
1
3
5
100
999
1000
EOF

cat <<EOF > "$expected_1"
First
Second
First
First
Second
First
EOF


cat <<EOF > "$input_2"
17
622
250
676
720
760
13
410
751
17
334
529
700
832
389
466
117
122
EOF

cat <<EOF > "$expected_2"
First
First
First
Second
First
First
First
First
First
First
First
First
First
First
First
Second
First
EOF
