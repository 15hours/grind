import pytest

from problem_1020 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "bfs" : sol.bfs_approach,
        "dfs" : sol.dfs_approach,
        "dsu" : sol.dsu_approach,
    }
    return method_solution_map[method]

def test_1(solution):
    assert solution([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]) == 3

def test_2(solution):
    assert solution([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]) == 0