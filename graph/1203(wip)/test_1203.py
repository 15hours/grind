import pytest

from problem_1203 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "kahn": sol.kahn_approach,
    }
    return method_solution_map[method]


def test_1(solution):
    assert solution(8,
                    2,
                    [-1, -1, 1, 0, 0, 1, 0, -1],
                    [[], [6], [5], [6], [3, 6], [], [], []]) \
        == [6, 3, 4, 1, 5, 2, 0, 7]
