#!/bin/bash
source ./create_tests.sh

cd tests_data
tests_num=$(find . -maxdepth 1 -type f -name "input_*" | wc -l)

for test_case in `seq 1 ${tests_num}`; do
    input_file="input_${test_case}.txt"
    output_file="output_${test_case}.txt"
    expected_file="expected_${test_case}.txt"

    echo "----- TEST $test_case -----"
    
    if ! python3 ../solution.py < "$input_file" > "$output_file"; then
        echo "Error: Test $test_case failed to run"
        exit 1
    fi

    if ! diff "$output_file" "$expected_file"; then
        echo "Error: Test $test_case output does not match expected output"
        exit 1
    fi

    echo -e " TEST $test_case: OK\n"
done
