import pytest

from problem_1091 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "bfs" : sol.bfs_approach,
    }
    return method_solution_map[method]

def test_1(solution):
    assert solution([[0,1],
                     [1,0]]) == 2

def test_2(solution):
    assert solution([[0,0,0],
                     [1,1,0],
                     [1,1,0]]) == 4