import pytest

from problem_1466 import Solution


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
    assert solution(5, [[1,0],[1,2],[3,2],[3,4]]) == 2

def test_2(solution):
    assert solution(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]) == 3