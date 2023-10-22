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
        in [[6, 3, 4, 1, 5, 2, 0, 7],
            [6, 3, 4, 0, 7, 1, 5, 2],
            [6, 3, 4, 5, 2, 0, 7, 1]]


def test_2(solution):
    assert solution(8,
                    2,
                    [-1, -1, 1, 0, 0, 1, 0, -1],
                    [[], [6], [5], [6], [3], [], [4], []]) \
        == []


def test_3(solution):
    assert solution(5,
                    5,
                    [2, 0, -1, 3, 0],
                        [[2, 1, 3], [2, 4], [], [], []]) \
        in [[3, 2, 4, 1, 0], 
            [3, 4, 1, 3, 0],
            [2, 4, 1, 3, 0]]
 
def test_4(solution):
    assert solution(6,
                    3,
                    [2, 1, 2, 0, 1, 1],
                    [[1, 2, 3], [3, 4, 5], [], [], [3], []]) \
        in [[3, 5, 4, 1, 2, 0], [3, 4, 5, 1, 2, 0]]


def test_5(solution):
    assert solution(10,
                    4,
                    [0, 1, 1, 2, 3, -1, 0, 0, 0, 1],
                    [[2, 5], [3, 5, 4, 6, 8, 7, 2], [7], 
                     [], [], [], [], [], [], []]) \
        == []


def test_6(solution):
    assert solution(3,
                    1,
                    [-1, 0, -1], 
                    [[], [0], [1]]) \
        == [0, 1, 2]