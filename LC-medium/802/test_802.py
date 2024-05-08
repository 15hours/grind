import pytest

from problem_802 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "dfs" : sol.dfs_approach,
        "kahn" : sol.kahn_approach,
    }
    return method_solution_map[method]

def test_1(solution):
    assert solution([[1,2],[2,3],[5],[0],[5],[],[]]) == [2,4,5,6]

def test_2(solution):
    assert solution([[0,6,7,9],[],[],[],[2,6,8],[7,9],[7,8,9],[],[6,9],[7]]) \
            == [1,2,3,5,7,9]