import pytest
import pandas as pd

from problem_1517 import valid_emails


@pytest.fixture
def solution():
    return valid_emails

def test_1(solution):
    data = [[1, 'Winston', 'winston@leetcode.com'], 
            [2, 'Jonathan', 'jonathanisgreat'], 
            [3, 'Annabelle', 'bella-@leetcode.com'], 
            [4, 'Sally', 'sally.come@leetcode.com'], 
            [5, 'Marwan', 'quarz#2020@leetcode.com'], 
            [6, 'David', 'david69@gmail.com'], 
            [7, 'Shapiro', '.shapo@leetcode.com']]
    Users = pd.DataFrame(
                    data, 
                    columns=['user_id', 'name', 'mail'])\
              .astype({'user_id':'int64', 
                       'name':'object', 
                       'mail':'object'})
                       
    result = solution(Users)
    expected =  pd.DataFrame(
                        {'user_id' : [1,3,4],
                         'name' : ['Winston', 'Annabelle', 'Sally'],
                         'mail' : ['winston@leetcode.com',
                                   'bella-@leetcode.com',
                                   'sally.come@leetcode.com']},
                        index = [0,2,3])
                        
    assert result.equals(expected)
