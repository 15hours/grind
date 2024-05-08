import pytest

from problem_207 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "kahn" : sol.kahn_approach,
        "dfs" : sol.dfs_approach
    }
    return method_solution_map[method]

def test_1(solution):
    assert solution(2, [[1,0]]) == True

def test_2(solution):
    assert solution(2, [[1,0],[0,1]]) == False

def test_3(solution):
    assert solution(3, [[1,0],[2,1],[0,2]]) == False

def test_4(solution):
    assert solution(3, [[1,0],[2,1],[2,0]]) == True

def test_5(solution):
    assert solution(3, [[1,0],[2,1],[2,2]]) == False

def test_6(solution):
    assert solution(3, [[0,1],[0,2],[1,2]]) == True

def test_7(solution):
    assert solution(3, [[1,0],[1,2],[0,1]]) == False

def test_8(solution):
    assert solution(5, [[1,4],[2,4],[3,1],[3,2]]) == True

def test_9(solution):
    assert solution(20, [[0,10],[3,18],[5,5],[6,11],
                         [11,14],[13,1],[15,1],[17,4]]) == False
    
def test_10(solution):
    assert solution(7, [[1,0],[0,3],[0,2],[3,2],
                        [2,5],[4,5],[5,6],[2,4]]) == True
    
def test_11(solution):
    assert solution(8, [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]) == False