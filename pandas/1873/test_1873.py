import pytest
import pandas as pd

from problem_1873 import calculate_special_bonus


@pytest.fixture
def solution():
    return calculate_special_bonus

def test_1(solution):
    data = [[2, 'Meir', 3000], 
            [3, 'Michael', 3800], 
            [7, 'Addilyn', 7400], 
            [8, 'Juan', 6100], 
            [9, 'Kannon', 7700]]
    Employees = pd.DataFrame(
                        data, 
                        columns=['employee_id', 'name', 'salary'])\
                  .astype({'employee_id':'int64', 
                           'name':'object', 
                           'salary':'int64'})
    
    result = solution(Employees)
    expected = pd.DataFrame(
                        {'employee_id' : [2,3,7,8,9],
                         'bonus' : [0.0, 0.0, 7400.0, 0.0, 7700.0]})
    
    assert result.equals(expected)