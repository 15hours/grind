import pytest

from solution import Solution


@pytest.fixture
def solution_res(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "bf": sol.bf_approach,
        "dp_td": sol.dp_top_down_approach,
        "dp_bu": sol.dp_bottom_up_approach,
        "fib_num": sol.fibbonaci_number_approach,
    }
    return method_solution_map[method]


def test_1(solution_res):
    assert solution_res(2) == 2


def test_2(solution_res):
    assert solution_res(3) == 3


def test_3(solution_res):
    assert solution_res(5) == 8


def test_4(solution_res):
    assert solution_res(45) == 1836311903
