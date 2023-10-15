import pytest

from problem_1514 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
            "dijkstra": sol.dijkstra_approach,
            "bf2": sol.bf_with_two_arrays_approach,
            "bf1": sol.bf_with_one_array_approach,
            "spfa": sol.spfa_approach,
    }
    return method_solution_map[method]

def test_1(solution):
    num_nodes = 3
    edges =     [[0,1],[1,2],[0,2]]
    succ_prob = [0.5,0.5,0.2]
    src =       0
    dst =       2
    assert solution(num_nodes, edges, succ_prob, src, dst) == 0.25000


def test_2(solution):
    num_nodes = 3
    edges =     [[0,1],[1,2],[0,2]]
    succ_prob = [0.5,0.5,0.3]
    src =       0
    dst =       2
    assert solution(num_nodes, edges, succ_prob, src, dst) == 0.30000

def test_3(solution):
    num_nodes = 3
    edges =     [[0,1]]
    succ_prob = [0.5]
    src =       0
    dst =       2
    assert solution(num_nodes, edges, succ_prob, src, dst) == 0.00000