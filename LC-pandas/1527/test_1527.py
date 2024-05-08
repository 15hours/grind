import pytest
import pandas as pd

from problem_1527 import find_patients


@pytest.fixture
def solution():
    return find_patients

def test_1(solution):
    data = [[1, 'Daniel', 'YFEV COUGH'], 
            [2, 'Alice', ''], 
            [3, 'Bob', 'DIAB100 MYOP'], 
            [4, 'George', 'ACNE DIAB100'],
            [5, 'Alain', 'DIAB201']]
    Patients = pd.DataFrame(
                        data, 
                        columns=['patient_id', 'patient_name', 'conditions'])\
                 .astype({'patient_id':'int64', 
                          'patient_name':'object', 
                          'conditions':'object'})

    result = solution(Patients)
    expected = pd.DataFrame(
                        {'patient_id' : [3,4],
                         'patient_name' : ['Bob', 'George'],
                         'conditions' : ['DIAB100 MYOP', 'ACNE DIAB100']},
                        index = [2,3])

    assert result.equals(expected)