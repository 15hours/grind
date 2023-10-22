import pytest

from problem_70 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "bf": sol.bf_approach,
        "dp_td": sol.dp_top_down_approach,
        "dp_bu": sol.dp_bottom_up_approach,
        "fib_num": sol.fibbonaci_number_approach,
    }
    return method_solution_map[method]


def test_1(solution):
    assert solution(2) == 2


def test_2(solution):
    assert solution(3) == 3


def test_3(solution):
    assert solution(5) == 8


def test_4(solution):
    assert solution(45) == 1836311903
