import pytest

from problem_1584 import Solution


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
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    assert solution(points) == 20


def test_2(solution):
    points = [[3,12],[-2,5],[-4,1]]
    assert solution(points) == 18


def test_3(solution):
    points = [[-8,14],[16,-18],[-19,-13],[-18,19],
              [20,20],[13,-20],[-15,9],[-4,-8]]
    assert solution(points) == 139