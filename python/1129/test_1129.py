import pytest

from problem_1129 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "bfs": sol.bfs_approach,
    }
    return method_solution_map[method]


def test_1(solution):
    assert solution(3, [[0, 1]], [[2, 1]]) == [0, 1, -1]


def test_2(solution):
    assert solution(5,
                    [[0, 1], [1, 2], [2, 3], [3, 4]],
                    [[1, 2], [2, 3], [3, 1]]) \
        == [0, 1, 2, 3, 7]
