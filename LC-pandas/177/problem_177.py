'''
#indexing

Write a solution to find the nth highest salary from the Employee 
table. If there is no nth highest salary, return null.

The result format is in the following example.

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
'''
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary = employee['salary'].drop_duplicates()\
                               .sort_values(ascending=False)
    
    if N > len(salary):
        return pd.DataFrame(
                    {'getNthHighestSalary({})'.format(N) : [None]})
    
    nth_salary = salary.iloc[N - 1]
    output = pd.DataFrame(
                {'getNthHighestSalary({})'.format(N): [nth_salary]})
    print(output)
    return output