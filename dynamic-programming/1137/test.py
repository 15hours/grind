import pytest

from solution import Solution


@pytest.fixture
def solution_res(pytestconfig):
    method = pytestconfig.getoption('--name')
    sol = Solution()
    method_solution_map = {
        "formula": sol.formula_approach,
        "dp_td": sol.dp_top_down_approach,
        "dp_bu": sol.dp_bottom_up_approach,
    }
    return method_solution_map[method]


def test_1(solution_res):
    assert solution_res(4) == 4


def test_2(solution_res):
    assert solution_res(25) == 1389537
