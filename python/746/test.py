import pytest

from solution import Solution


@pytest.fixture
def solution_res(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "brute_force": sol.bf_approach,
        "memoization": sol.dp_top_down_approach,
        "tabulation": sol.dp_bottom_up_approach,
        "const_space": sol.dp_bottom_up_const_approach,
    }
    return method_solution_map[method]


def test_1(solution_res):
    assert solution_res([10, 15, 20]) == 15


def test_2(solution_res):
    assert solution_res([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
