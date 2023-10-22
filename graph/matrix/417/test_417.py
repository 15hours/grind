import pytest

from problem_417 import Solution


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
    assert sorted(solution([[1,2,2,3,5],
                            [3,2,3,4,4],
                            [2,4,5,3,1],
                            [6,7,1,4,5],
                            [5,1,1,2,4]])) \
            == sorted([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])
    
def test_2(solution):
    assert solution([[1]]) == [[0, 0]]