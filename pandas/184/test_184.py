import pytest
import pandas as pd

from problem_184 import department_highest_salary


@pytest.fixture
def solution():
    return department_highest_salary

def test_1(solution):
    data = [[1, 'Joe', 70000, 1], 
            [2, 'Jim', 90000, 1], 
            [3, 'Henry', 80000, 2], 
            [4, 'Sam', 60000, 2], 
            [5, 'Max', 90000, 1]]
    Employee = pd.DataFrame(
                        data, 
                        columns=['id', 'name', 'salary', 'departmentId'])\
                 .astype({'id':'Int64', 
                          'name':'object', 
                          'salary':'Int64', 
                          'departmentId':'Int64'})

    data = [[1, 'IT'], 
            [2, 'Sales']]
    Department = pd.DataFrame(
                        data, 
                        columns=['id', 'name'])\
                   .astype({'id':'Int64', 
                            'name':'object'})
    
    result = solution(Employee, Department)
    expected = pd.DataFrame(
                        {'Department' : ['IT', 'Sales', 'IT'],
                         'Employee' : ['Jim', 'Henry', 'Max'],
                         'Salary' : [90_000, 80_000, 90_000]})
    
    return result.equals(expected)