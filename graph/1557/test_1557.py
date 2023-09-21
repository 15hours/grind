import pytest

from problem_1557 import Solution


@pytest.fixture
def solution():
    sol = Solution()
    return sol.findSmallestSetOfVertices

def test_1(solution):
    assert solution(6, [[0,1],[0,2],[2,5],[3,4],[4,2]]) == [0,3]

def test_2(solution):
    assert solution(5, [[0,1],[2,1],[3,1],[1,4],[2,4]]) == [0,2,3]