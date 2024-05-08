import pytest
import pandas as pd

from problem_1757 import find_products


@pytest.fixture
def solution():
    return find_products

def test_1(solution):
    data = [['0', 'Y', 'N'], 
            ['1', 'Y', 'Y'], 
            ['2', 'N', 'Y'], 
            ['3', 'Y', 'Y'], 
            ['4', 'N', 'N']]
    Products = pd.DataFrame(
                        data, 
                        columns=['product_id', 'low_fats', 'recyclable'])\
                  .astype({'product_id':'int64', 
                           'low_fats':'category', 
                           'recyclable':'category'})
                    
    result = solution(Products)
    expected = pd.DataFrame(
                        {'product_id' : [1, 3]},
                        index = [1, 3])

    assert result.equals(expected)
