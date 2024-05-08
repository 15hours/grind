import pytest
import pandas as pd

from problem_595 import big_countries


@pytest.fixture
def solution():
    return big_countries

def test_1(solution):
    data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], 
            ['Albania', 'Europe', 28748, 2831741, 12960000000], 
            ['Algeria', 'Africa', 2381741, 37100000, 188681000000], 
            ['Andorra', 'Europe', 468, 78115, 3712000000], 
            ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
    
    World = pd.DataFrame(
                    data, 
                    columns=['name', 
                             'continent', 
                             'area', 
                             'population', 
                             'gdp'])\
               .astype({'name':'object', 
                        'continent':'object', 
                        'area':'Int64', 
                        'population':'Int64', 
                        'gdp':'Int64'})
    
    result = solution(World)
    expected= pd.DataFrame(
                     {'name' : ['Afghanistan', 'Algeria'],
                      'population' : [25500100, 37100000],
                      'area' : [652230, 2381741]},
                     index = [0, 2])
    
    result_list = result.values.tolist()
    expected_list = expected.values.tolist()
    
    assert result_list == expected_list