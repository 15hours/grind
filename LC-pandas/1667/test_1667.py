import pytest
import pandas as pd

from problem_1667 import fix_names


@pytest.fixture
def solution():
    return fix_names

def test_1(solution):
    data = [[1, 'aLice'], 
            [2, 'bOB']]
    Users = pd.DataFrame(
                    data, 
                    columns=['user_id', 'name'])\
              .astype({'user_id':'Int64', 
                       'name':'object'})
    
    result = solution(Users)
    expected = pd.DataFrame(
                        {'user_id' : [1,2],
                         'name' : ['Alice', 'Bob']})
    
    result_list = result.values.tolist()
    expected_list = expected.values.tolist()
    
    assert result_list == expected_list