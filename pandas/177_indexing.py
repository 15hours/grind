# Write a solution to find the nth highest salary from the Employee table. 
# If there is no nth highest salary, return null.

# The result format is in the following example.

# Example 1:
# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# n = 2
# Output: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | 200                    |
# +------------------------+

# Example 2:
# Input: 
# Employee table:
# | id | salary |
# | -- | ------ |
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# n = 1
# Output: 
# +------------------------+
# | getNthHighestSalary(1) |
# +------------------------+
# | 300                   |
# +------------------------+

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary = employee['salary'].drop_duplicates().sort_values(ascending=False) #ascending = False because nth is not by index but by sorted list
    print(salary, N)
    if N > len(salary):
        return pd.DataFrame(
            {'getNthHighestSalary({})'.format(N): [None]}
        )
    nth_salary = salary.iloc[N - 1]
    return pd.DataFrame(
            {'getNthHighestSalary({})'.format(N): [nth_salary]}
    )
    
    
data = [[1, 100], [2, 200], [3, 300]]
Employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
N = 1
print(nth_highest_salary(Employee, N))