import pytest

from problem_787 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "dp": sol.dp_approach,
        "bf": sol.basic_bf_approach,
    }
    return method_solution_map[method]


def test_1(solution):
    num_cities = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    stops = 1

    assert solution(num_cities, flights, src, dst, stops) == 700


def test_2(solution):
    num_cities = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    stops = 1

    assert solution(num_cities, flights, src, dst, stops) == 200


def test_3(solution):
    num_cities = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    stops = 0

    assert solution(num_cities, flights, src, dst, stops) == 500


def test_4(solution):
    num_cities = 5
    flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
    src = 0
    dst = 2
    stops = 2

    assert solution(num_cities, flights, src, dst, stops) == 7