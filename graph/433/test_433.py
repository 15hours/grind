import pytest

from problem_433 import Solution


@pytest.fixture
def solution(pytestconfig):
    method = pytestconfig.getoption("--name")
    sol = Solution()
    method_solution_map = {
        "bfs" : sol.bfs_approach,
    }
    return method_solution_map[method]

def test_1(solution):
    assert solution("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1
    
def test_2(solution):
    assert solution("AACCGGTT", 
                    "AAACGGTA", 
                    ["AACCGGTA","AACCGCTA","AAACGGTA"]) == 2
    