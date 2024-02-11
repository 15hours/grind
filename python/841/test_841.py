import pytest

from problem_841 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "dfs" : sol.dfs_approach,
    }
    return method_solution_map[method]

def test_1(solution):
    assert solution([[1],[2],[3],[]]) == True

def test_2(solution):
    assert solution([[1,3],[3,0,1],[2],[0]]) == False