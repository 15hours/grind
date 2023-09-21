import pytest

from problem_997 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "one" : sol.one_array_approach,
        "two" : sol.two_array_approach,
    }
    return method_solution_map[method]

def test_1(solution):
    assert solution(2, [[1,2]]) == 2

def test_2(solution):
    assert solution(3, [[1,3],[2,3]]) == 3

def test_3(solution):
    assert solution(3, [[1,3],[2,3],[3,1]]) == -1