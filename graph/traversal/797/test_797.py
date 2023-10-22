import pytest

from problem_797 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "bfs" : sol.bfs_approach,
        "dfs" : sol.dfs_approach,
        "dp" : sol.dp_approach,
    }
    return method_solution_map[method]

def test_1(solution):
    assert solution([[1,2],[3],[3],[]]) == [[0,1,3],[0,2,3]]

def test_2(solution):
    assert sorted(solution([[4,3,1],[3,2,4],[3],[4],[]])) \
            == sorted([[0,4],[0,3,4],[0,1,4],[0,1,3,4],[0,1,2,3,4]])