import pytest
from graph.problem_210 import Solution

@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "kahn" : sol.kahn_approach,
        "dfs" : sol.dfs_approach,
    }
    return method_solution_map[method]
    
def test_1(solution):
    assert solution(2, [[1,0]]) == [0,1]

def test_2(solution):
    assert solution(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,1,2,3]

def test_3(solution):
    assert solution(3, [[1,0],[2,1],[0,2]]) == []

def test_4(solution):
    assert solution(4, [[0,3],[1,3],[2,0],[2,1]]) == [3, 0, 1, 2]
