import pytest

from problem_1376 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "bfs" : sol.bfs_approach,
        "dfs" : sol.dfs_approach,
    }
    return method_solution_map[method]

def test_1(solution):
    assert solution(1, 0, [-1], [0]) == 0

def test_2(solution):
    assert solution(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]) == 1