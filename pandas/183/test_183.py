import pytest
import pandas as pd

from problem_183 import find_customers


@pytest.fixture
def solution():
    return find_customers

def test_1(solution):
    data_customers = [[1, 'Joe'],
                      [2, 'Henry'],
                      [3, 'Sam'],
                      [4, 'Max']]
    Customers = pd.DataFrame(
                        data_customers, 
                        columns=['id', 'name'])\
                  .astype({'id':'Int64', 
                           'name':'object'})
    
    data_orders = [[1, 3], 
                   [2, 1]]
    Orders = pd.DataFrame(
                    data_orders, 
                    columns=['id', 'customerId'])\
               .astype({'id':'Int64', 
                        'customerId':'Int64'})
    
    assert solution(Customers, Orders)\
            .equals(pd.DataFrame(
                            {"Customers" : ["Henry", "Max"]},
                            index = [1, 3]))