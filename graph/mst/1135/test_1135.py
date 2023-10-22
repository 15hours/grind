import pytest

from problem_1135 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "kruskal": sol.kruskal_approach,
        "prim": sol.prim_approach,
    }
    return method_solution_map[method]


def test_1(solution):
    n = 3
    connections = [[1,2,5],[1,3,6],[2,3,1]]
    assert solution(n, connections) == 6
    

def test_2(solution):
    n = 4
    connections = [[1,2,3],[3,4,4]]
    assert solution(n, connections) == -1
