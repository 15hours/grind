import pytest

from problem_1306 import Solution


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
    assert solution([4,2,3,0,3,1,2], 5) == True

def test_2(solution):
    assert solution([4,2,3,0,3,1,2], 0) == True

def test_3(solution):
    assert solution([3,0,2,1,2], 2) == False