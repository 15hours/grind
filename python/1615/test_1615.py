import pytest

from problem_1615 import Solution


@pytest.fixture
def solution():
    sol = Solution()
    return sol.maximal_network_rank

def test_1(solution):
    assert solution(4, [[0,1],[0,3],[1,2],[1,3]]) == 4

def test_2(solution):
    assert solution(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]) == 5

def test_3(solution):
    assert solution(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]) == 5