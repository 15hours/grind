import pytest

from problem_839 import Solution


# method = "dfs"
method = "dsu"

@pytest.fixture
def solution():
    sol = Solution()
    method_solution_map = {
        "dfs": sol.dfs_approach,
        "dsu": sol.dsu_approach,
    }
    return method_solution_map[method]

def test_1(solution):
    assert solution(["tars","rats","arts","star"]) == 2

def test_2(solution):
    assert solution(["omv","ovm"]) == 1

def test_3(solution):
    assert solution(["tars", "arts", "rats", "start"]) == 2

def test_4(solution):
    assert solution(["abc","abc"]) == 1
    
def test_5(solution):
    assert solution(["ajdidocuyh","djdyaohuic",
                     "ddjyhuicoa","djdhaoyuic",
                     "ddjoiuycha","ddhoiuycja",
                     "ajdydocuih","ddjiouycha",
                     "ajdydohuic","ddjyouicha"]) == 2

if __name__ == "__main__":
    pytest.main(["--tb=short", "-v", "-rxXs", "-s"])