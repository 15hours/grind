import pytest
import pandas as pd

from problem_1148 import article_views


@pytest.fixture
def solution():
    return article_views

def test_1(solution):
    data = [[1, 3, 5, '2019-08-01'], 
            [1, 3, 6, '2019-08-02'], 
            [2, 7, 7, '2019-08-01'], 
            [2, 7, 6, '2019-08-02'], 
            [4, 7, 1, '2019-07-22'], 
            [3, 4, 4, '2019-07-21'], 
            [3, 4, 4, '2019-07-21']]
    Views = pd.DataFrame(
                    data, 
                    columns=['article_id', 'author_id', 
                             'viewer_id', 'view_date'])\
               .astype({'article_id':'Int64', 
                        'author_id':'Int64', 
                        'viewer_id':'Int64', 
                        'view_date':'datetime64[ns]'})
    
    result = solution(Views)
    expected = pd.DataFrame(
                        {'id' : [4, 7]},
                        index = [5, 2])
    result_list = result.values.tolist()
    expected_list = expected.values.tolist()
    
    assert result_list == expected_list