import pytest
import pandas as pd

from problem_177 import nth_highest_salary


@pytest.fixture
def solution():
    return nth_highest_salary

def test_1(solution):
    data = [[1, 100], [2, 200], [3, 300]]
    Employee = pd.DataFrame(
                    data, 
                    columns=['id', 'salary'])\
                 .astype({'id':'int64', 
                          'salary':'int64'})
    N = 1
    assert solution(Employee, N) \
            .equals(pd.DataFrame({'getNthHighestSalary(1)': [300]}))