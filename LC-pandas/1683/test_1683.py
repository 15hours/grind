import pytest
import pandas as pd

from problem_1683 import invalid_tweets


@pytest.fixture
def solution():
    return invalid_tweets

def test_1(solution):
    data = [[1, 'Vote for Biden'], 
            [2, 'Let us make America great again!']]
    Tweets = pd.DataFrame(
                    data, 
                    columns=['tweet_id', 'content'])\
               .astype({'tweet_id':'Int64', 
                        'content':'object'})

    result = solution(Tweets)
    expected = pd.DataFrame(
                        {'tweet_id' : [2]},
                        index = [1])

    result_list = result.values.tolist()
    expected_list = expected.values.tolist()

    assert result_list == expected_list
