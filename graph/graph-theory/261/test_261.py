import pytest

from problem_261 import Solution


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
    assert solution(5, [[0,1],[0,2],[0,3],[1,4]]) == True

def test_2(solution):
    assert solution(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]) == False